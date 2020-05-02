from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CommonInfo(models.Model):
    
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now = True,null=True)

    class Meta :
        abstract = True
        ordering = ['-created_on']

    """  
    Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. 
    """


class Question(CommonInfo):

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(null=True)
    

    def __str__(self):
        return self.title

    # Reverse relationship : return the choices related to question

    @property
    def choices(self):
        return self.choice_set.all()   
        # return obj_question.Choice_set.all()

    """ 
    
    The reason the reverse is a queryset is, ForeignKey is 1-to-many relationship. Hence, the reverse is a queryset
    The _set object is made available when related_name is not specified.
    
     """    

class Choice(CommonInfo):

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.text

    # return : which choice got how many votes
    @property
    def votes(self):
        return self.answer_set.count()

    @property
    def total_votes(self):
        # values() returns Python dictionaries, instead of a QuerySet object:
        value = self.answer_set.values()
        print("### model # ",value)
        user = []
        for i in value:
            print("## for : ",i)
            print("Answer id : ",i['id'])
            print("User id (who answerd) : ",i['user_id'])
            print("Choice id : ",i['choice_id'])

            user.append(User.objects.get(id= i['user_id']))
            

        print("### totol total total ###",user)

    # You can also specify which fields you want returned:
    # value = self.answer_set.values('user_id','choice_id') 

        return [i['user_id'] for i in value]

    @property
    def who_voted(self):
       
        value = self.answer_set.values('user_id') 
        user = []
      
        for i in value:
            user.append(User.objects.get(id= i['user_id']))
       
        return user
   

class Answer(CommonInfo):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)

    def __str__(self):

        return self.user.first_name + ' - ' + self.choice.text



class Demo(CommonInfo) :

    end_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.end_date)