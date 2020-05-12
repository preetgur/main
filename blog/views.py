from django.shortcuts import render,redirect,HttpResponse
from .forms import Blog_Form,Images_Form,ProfileForm
from .models import Blog,Images

# Create your views here.

def index(request):

    context = {}
    return render(request,"blog/index.html",context)

def dashboard(request):
    
    # blog = Blog.objects.all()
    context = { 
        "comment":Comment.objects.filter(user= request.user,parent__isnull=True),
        "replies":Comment.objects.filter(user=request.user,parent__isnull=False),
        "like_comments":Like.objects.filter(users=request.user,comment__parent__isnull=False),
        "like_replies":Like.objects.filter(users=request.user,comment__parent__isnull=True),

        "dis_like_comments":DisLike.objects.filter(users=request.user,comment__parent__isnull=False),
        "dis_like_replies":DisLike.objects.filter(users=request.user,comment__parent__isnull=True),

    }
    
    return render(request,"blog/dashboard.html",context)


def create_blog(request):
    
    form = Blog_Form()
    image_form = Images_Form()

    data = Blog.objects.all().order_by('-created_on')

    if request.method == "POST":
        form = Blog_Form(request.POST)
        image_form = Images_Form(request.POST,request.FILES)
        
        if form.is_valid() and image_form.is_valid() :
         
            # remember in the forms.py file only includes the fields which use submit
            # from frontend 
            poll = form.save(commit=False)  # used to store the data filled by user
            poll.created_by = request.user
            poll.save()

            img = image_form.save(commit=False)
            img.blog = poll
            img.save()

            return redirect("show_blogs")

        else : 
            print("some error in validation ")        
    context = {
        "form":form,
        "data":data,
        "image_form":image_form,
        }
    return render(request,"blog/all_blogs.html",context)



def show_blogs(request):

    blogs = Blog.objects.all().order_by('-created_on')
  

    context = { 
        "blogs":blogs,
        "images" : Images.objects.all,

    }
    return render(request,"blog/show_blogs.html",context)


from .models import Comment,User_Additional_Info
from .forms import Comment_Form

def detail_blog(request ,pk):
    ab =User_Additional_Info.objects.get(users=request.user)
    print("@#@#@#@#@#@##@ ",ab)
    # Get the Blog with the help of "pk"
    blog = Blog.objects.get(id = pk)
    blogs = Blog.objects.all().order_by('-created_on')

    # Feteching comment related to that post
    form = Comment_Form()
    if request.method == "POST":
        message = request.POST.get('message')
        form = Comment_Form(request.POST)

        if form.is_valid():

   
            # How to reply to comment
            """ 
            We add a QuerySet to retrieve all parent active comments for this post. After this, we validate the submitted data using the form's is_valid(). If the form is valid we check if submitted data comes from hidden input in replay button form. Next if parent_id exits we create parent object(parent_obj) for replay comment and replay_comment object, then we assign parent_obj to replay_comment. If parent_obj is equal to None we just proceed with normal comment by creating new_comment object and saving it to the database.
            """

            """
            Difference bw a "comment" and "reply" :
                commnet : doesn't have any field value associated with it .
                reply : have the hidden value as the "comment id" each of blog.when comment is created only then we have it's id.
            """
            comment_instance = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                comment_id = int(request.POST.get('comment_id'))
                print("#### parent id #### ",comment_id)

            except:
                comment_id = None
            # if parent_id has been submitted get parent_obj id 
            if comment_id:
                comment_instance = Comment.objects.get(id=comment_id)  # Get the specific comment to whom the reply is given.
                print("#### comment Object #####",comment_instance)
                # if parent object exist
                # then it is reply to some comment

                if comment_instance:
                    # create replay comment object
                    replay_comment = form.save(commit=False)  # data got from the html form
                    # assign comment_obj to replay comment
                    replay_comment.parent = comment_instance    # set the parent as comment id   
                    # same work as below
                    replay_comment.user = request.user
                    replay_comment.blog = blog
                
                    replay_comment.save()
                    print("This is reply to some comment ##",replay_comment)

                    

            
            ### Adding the comment #### 
            # Below code is common bw comment and relpy
            comment = form.save(commit=False) # Hold the message from html and then append the data with it.
            comment.blog = blog
            comment.user = request.user
            comment.save()   # save the comment
            print(" comment ### ",comment)

            return redirect(f"/detail/{blog.id}")
            

    context = {
        "i": blog,
        "blogs":blogs,
        "comments":Comment.objects.filter(blog = blog , parent__isnull=True).order_by('-timestamp'),
        "form":form,
        "total_comments":Comment.objects.filter(blog=blog,parent__isnull=True).count(),
        "user_additional":User_Additional_Info.objects.get(users=blog.created_by),


        }
    return render(request,"blog/blog_detail.html",context)

from django.conf import settings  
from django.core.mail import send_mail

def sendEmail(subject,message,recepient):
   
    try :
        send_mail(subject, 
        message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
    
    except Exception as e:
        print("some eror occured while sending email ##",e)

from .models import Like,DisLike
from django.contrib import messages
def like(request,*args,**kwargs):

    comment_id = kwargs.get('comment_id', None)
    option = kwargs.get('option', None) 
    blog_id = kwargs.get('blog_id', None) 

    comment = Comment.objects.get(id = comment_id)
    print("#### comment id ## ",comment_id,option,blog_id)


    try:
        # If child DisLike model doesnot exit then create
        # "dis_likes" is thorogh reverse relationship
        # DisLike models has comment field which has onetoone
        comment.dis_likes
    except :
        DisLike.objects.create(comment = comment)

    try:
        # If child DisLike model doesnot exit then create
        comment.likes
    except :
        Like.objects.create(comment = comment)

    if option.lower() == 'like':

        if request.user in comment.likes.users.all():
            # "likes" is the related_name in Like models to "Comment" models
            comment.likes.users.remove(request.user)
        else:    
            comment.likes.users.add(request.user)
            comment.dis_likes.users.remove(request.user)
    
        # send notification to user that someone like your comment
         
            if request.user == comment.user:
                print("##### Ower of comment ####")

            elif request.user != comment.user:
                print("#### someone liked your comment ####") 
                subject = 'Someone liked your comment'
                message = f' "{request.user}" Liked your comment.' # logged in user
                recepient = f'{comment.user.email}' # who created the comment

                try :
                    sendEmail(subject=subject,message=message,recepient=recepient)
                
                except Exception as e:
                    print("some eror occured while sending email ##",e)
   

    elif option.lower() == 'dis_like':

        if request.user in comment.dis_likes.users.all():
            comment.dis_likes.users.remove(request.user)
        else:    
            comment.dis_likes.users.add(request.user)
            comment.likes.users.remove(request.user)

    return redirect(f"/detail/{blog_id}")


################

def profile(request):

    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        opt = request.POST['option_1']
        

        print("####### option ",opt)

        names = [(k,v) for k, v in request.POST.items() if k.startswith('option_')]
        print("####### name ",names,len(names))

        print("form ############3 ",form)

        if form.is_valid():
            form.save()
            return redirect("show_blogs")

        else:
            print("Some error")


    context = { "form":form}
    return render(request,"blog/profile.html",context)


from .forms import Profile_Form,Choice_Form
from .models import ProfileInterest
def question(request):

    p = Profile_Form()
    # c = Choice_Form()

    if request.method == "POST":
        p = Profile_Form(request.POST)
        opt = request.POST['option_1']
        
        # get all the values starts with name "option_" in html form
        options = [value for key, value in request.POST.items() if key.startswith('option_')]
       
        if p.is_valid():
            ab = p.save()  # saved form is store in varible so that it can be linked with other models

            for i in options :
                obj = ProfileInterest()
                obj.profile =  ab       # choice related to question
                obj.interest = i
                obj.save()


            return HttpResponse("< Saved>")

    context = { "form":p}
    return render(request,"blog/profile.html",context)



########################## Rest api Person and Person Inereset
from blog.serializers import Profile_Serializer,ProfileInterest_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# create Profile
@api_view(['GET', 'POST'])
def profile_api(request):
    
    if request.method == "GET":
        serializer = Profile_Serializer()
        seri = ProfileInterest_Serializer()

    if request.method =="POST":
        serializer = Profile_Serializer(data=request.data)
        seri = ProfileInterest_Serializer(data= request.data)
        
        if serializer.is_valid() and seri.is_valid():
            print(serializer.validated_data)  # return ordered dict
            
            serializer.save()
            seri.save()
            return HttpResponse("Saved in database")

    return Response(serializer.data)


# List of all Profiles
from blog.models import Profile
@api_view(['GET','POST'])
def all_profile_api(request):

    qs =  Profile.objects.all().order_by('-id')[:5] # Recent 5 profiles
    serializer = Profile_Serializer(qs,many=True)
    return Response(serializer.data)