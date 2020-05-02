from .models import Question,Answer,Choice
from django import forms

class Question_Form(forms.ModelForm):

    class Meta :
        model = Question
        fields = ['title']


class Choice_Form(forms.ModelForm):

    # converting the text field into char field

    text = forms.CharField(max_length=20)

    class Meta :
        model = Choice
        exclude = ('question',)


class Answer_Form(forms.ModelForm):

    class Meta :
        model = Answer
        fields = "__all__"





from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_Creation_Form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1','password2','groups']
   
                