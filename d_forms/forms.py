from django import forms 

class Contact_Form(forms.Form):
    name = forms.CharField(required=True)
    comment = forms.CharField(max_length=5)