from django.shortcuts import render
from .forms import Question_Form,Choice_Form,Answer_Form
from .models import Choice,Answer,Question
from django.shortcuts import HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import voted_already,admin_only
from django.contrib.auth.decorators import login_required 


def home(request):

    return render(request,"poll/poll_index.html")

# Create your views here.
@login_required(login_url="login")
@admin_only
def index(request):

    recent_question = Question.objects.all().order_by('-created_on')
    total = Question.objects.count()


    # List comprehension
    # return choice_form with same 'name' and 'required_id' in html
    # choice_form = [Choice_Form() for x in range(0,3)] 

    # prefix : add the 'name' and 'required_id' according to for loop as "0-text,1-text"
    # To give each Form its own namespace, use the prefix keyword argument:
    # choice_form = [Choice_Form(prefix=str(x)) for x in range(0,3)]

    # instance = you can use it or not this does'nt efffect code
    choice_form = [Choice_Form(prefix=str(x),instance=Choice()) for x in range(1,4)]
    question_form = Question_Form()
    

    if request.method == "POST" :
       
        title = request.POST.get("title","")
        option1 = request.POST.get("1-text","")
       
        question_form = Question_Form(request.POST)
        choice_form = [Choice_Form(request.POST,prefix=str(x),instance=Choice()) for x in range(1,4)]
        print("### choice forms :",choice_form," Length",len(choice_form))
        if question_form.is_valid() and all( [ i.is_valid() for i in choice_form ] ):
   
            poll = question_form.save(commit=False)
            poll.created_by = request.user
            poll.save()

            # Iterate each choice form
            for i in choice_form:
               
                choice = i.save(commit=False)
                choice.question = poll
                choice.save()


            # return HttpResponse("ADDEd Poll with choices")
            return redirect("poll")

        else:
            print("Not valid")


        print("###",title,option1,option2,option3)

        # question_form = Question_Form(request.POST)

    context = {
        "question_form":question_form,
        "choice_form":choice_form,
        "recent_question": recent_question,
        "total":total
        }
    return render(request,"poll/index.html",context)



def total_polls(request):

    all_question = Question.objects.all().order_by('-created_on')
    total = Question.objects.count()
    user_data = ""
    # if request.user == "AnonymousUser":
    #     user_data = None


    # else :
    #     user_answer = request.user.answer_set.all()
    #     print("######33 user answer to question ######## ",user_answer)
    #     user_question = request.user.question_set.all()  
    #     #it only return the question that created by user
    #     print("######33 user answer to question ######## ",user_question)

    
   
    #     # convert two list into dictonary
    #     user_data =  dict(zip(user_question,user_answer))
   
    context = {
         "all_question":all_question,
         "total":total,
        #  "user_data":user_data,
         }
    return render(request,"poll/polls.html",context)

@login_required(login_url="login")
@voted_already
def give_vote(request,pk):

    question = Question.objects.get(id = pk)
   

    if request.method == "POST":
        

        choice_id = request.POST.get("answer")
        print("#### answer",choice_id)

        answer_obj = Answer()
        answer_obj.user = request.user
        answer_obj.choice = Choice.objects.get(id = choice_id)
        answer_obj.save()
        
        messages.success(request,"Your Answer is collected, Thanks For Your Time.")
        return redirect("total_polls")


    context = { "question":question
                }
    return render(request,"poll/give_vote.html",context)

@login_required(login_url="login")
def result(request,poll_id):

    poll = Question.objects.get(id = poll_id)
    
    print("!!!!!!!!!!!!!!!! ((((((())))))) Created on ,",poll.created_on)



    choice = Choice.objects.filter(question = poll_id)
    print("#### choicess ###",choice)
    
    logged_in_user = User.objects.get(id=request.user.id)

    li = []
    count = 0
    for i in choice:
        count += i.votes
        print("# viuews",i.total_votes)
        print("###################################### >> ",i.who_voted)

        if logged_in_user in i.who_voted:
            print("already voted => ",request.user)

        else :
            print("Welcome to the Poll Please Cast Your vote >> ",request.user)

        li.append(i.total_votes)
    print("################# ",li)    
    
    print("!!!!!!!!!!!!!!!!!!!!!!! ",count)
    username = []

    for i in li:

        comp = {l for l in i}
        print("comp ### ",comp)
        comp_list = list(comp)
        for j in comp_list:
            print("#### From list of list : ",j)
            user = User.objects.get(id =j)
            username.append(user)
            print("user Who voted : ",username)

    print("####### username #### : ",username)     
  
    context = {
        "poll":poll,
        # "total_answer":total_answer,
        "choice":choice,
        "user":username,
        "count":count
        }
    return render(request,"poll/result.html",context)


#################################### Create API ######################
from rest_framework.decorators import api_view
from rest_framework.response import Response   
from .serializers import Choice_Serializer

@api_view(['GET'])
def ajax_json_response(request,poll_id):


    poll = Question.objects.get(id = poll_id)
    
    choice = Choice.objects.filter(question = poll_id)
    
    serializer = Choice_Serializer(choice,many=True)
    
    
    return Response(serializer.data)




from poll.forms import User_Creation_Form
from django.contrib.auth.models import Group

def signup(request):

    form = User_Creation_Form()

    if request.method == "POST":

        form = User_Creation_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request,f"{username}, Accounts created Successfuly!")

            user_creation_form = form.save()

            group = Group.objects.get(name = 'user')
            user_creation_form.groups.add(group)  # adding the group

            # Adding entry to user_vote table
            # User_vote.objects.create(user = user_creation_form)

            return redirect('login')


    context = {"form":form}
    return render(request,"poll/signup.html",context)
