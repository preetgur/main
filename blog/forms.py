from django import forms
from blog.models import Blog,Images,Profile,ProfileInterest,Comment


class Blog_Form(forms.ModelForm):

    
    title = forms.CharField(max_length=100)

    class Meta :
        model = Blog
        fields = ['title','content']



class Images_Form(forms.ModelForm):
    
    class Meta :
        model = Images
        fields = ['pic']


class Comment_Form(forms.ModelForm):

    # message = forms.Textarea(attrs={'rows':4, 'cols':15})
    class Meta :
        model = Comment
        fields = ['message']

# profile form


# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100,required=True)
#     last_name = forms.CharField(max_length=100,required=True)
#     interest_0 = forms.CharField(max_length=100,required=True)
#     interest_1 = forms.CharField(max_length=100,required=True)
#     interest_2 = forms.CharField(max_length=100,required=True)

#     def save(self):
#         Profile = self.instance
#         print("############ Profile instace ",Profile)
#         Profile.first_name = self.cleaned_data["first_name"]
#         Profile.last_name = self.cleaned_data["last_name"]
#         Profile.save()
#         # Profile.interest_set.all().delete()
#         for i in range(3):  
#            interest = self.cleaned_data["interest_{}".format(i)]
#            ProfileInterest.objects.create(
#                profile=Profile, interest=interest)
        
        
#     class Meta:
        
#         model = Profile  # why not we use ProfileIntereset : because "ProfileInterest.profile" must be a "Profile" instance.
#         fields = "__all__"




class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        interests = ProfileInterest.objects.filter(
            profile=self.instance  # instance of user
        )
        for i in range(len(interests) + 1):
            field_name = 'interest_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = interests[i].interest
            except IndexError:
                self.initial[field_name] = ""
        # create an extra blank field
        field_name = 'interest_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False)

    def clean(self):
        interests = set()
        i = 0
        field_name = 'interest_%s' % (i,)
        while self.cleaned_data.get(field_name):
           interest = self.cleaned_data[field_name]
           if interest in interests:
               self.add_error(field_name, 'Duplicate')
           else:
               interests.add(interest)
           i += 1
           field_name = 'interest_%s' % (i,)
        self.cleaned_data["interests"] = interests

    def save(self):
        profile = self.instance
        profile.first_name = self.cleaned_data["first_name"]
        profile.last_name = self.cleaned_data["last_name"]
        profile.save()
        # profile.interest_set.all().delete()
        for interest in self.cleaned_data["interests"]:
           ProfileInterest.objects.create(
               profile=profile,
               interest=interest,
           )

    def get_interest_fields(self):
        for field_name in self.fields:
            if field_name.startswith("interest_"):
                print("####### Interset ######",field_name)
                yield self[field_name]


    class Meta:
        
        model = Profile  # why not we use ProfileIntereset : because "ProfileInterest.profile" must be a "Profile" instance.
        fields = "__all__"



####################

class Profile_Form(forms.ModelForm):

    class Meta : 
        model = Profile
        fields = "__all__"


class Choice_Form(forms.ModelForm):

    class Meta : 
        model = ProfileInterest
        fields = "__all__"        