from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.


class User_Additional_Info(models.Model):

    users = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,default="default.png")

    def __str__(self):
        return str(self.users.username) + str(self.mobile)

    @property
    def get_blog_list(self):
        return self.user_additional_info.count()

     

from ckeditor_uploader.fields import  RichTextUploadingField
class Blog(models.Model):

    title = models.TextField(max_length=100)
    content = RichTextUploadingField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_category = models.ManyToManyField('Blog_category',blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)

    @property
    def img(self):
        return self.images_set.values_list('pic')

    def __str__(self):
        return self.title 

    @property
    def display_my_safefield(self):
        # checking for "script tag" in content

        if "<script>" in self.content:
            self.is_malicious = True
            self.save()
            return self.content
            
        return mark_safe(self.content)   


class Blog_category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name



class Images(models.Model):
    pic = models.ImageField(null=True,blank=True,default="default.png")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # it is created in order to reply to comments
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):                      
        return  f"{self.message}  | by>> {self.user}"

    @property
    def get_total_likes(self):
        return self.likes.users.count()

    @property
    def get_total_dis_likes(self):
        return self.dis_likes.users.count()
        
    # @property
    # def get_total_replies(self): # total replies to each comment
    #     return self.replies.exclude(parent = None)


    # @property
    # def total_replies(self):
    #     return Comment.objects.filter(blog= self.blog,parent__isnull=True).count()



class Like(models.Model):
    ''' like  comment '''
    comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='user_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.message)[:30]

    
class DisLike(models.Model):
    ''' Dislike  comment '''
    comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='user_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.message)[:30]

# for using btn 

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name

class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)

    def __str__(self):
        return str(self.profile) + str(self.interest)