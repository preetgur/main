from rest_framework import serializers
from blog.models import Profile,ProfileInterest,Blog,Comment,Like,DisLike


class Like_Serializer(serializers.ModelSerializer):

    class Meta : 
        model = Like
        fields = ['comment']





class Profile_Serializer(serializers.ModelSerializer):

    class Meta :
        model = Profile
        fields = "__all__"



class ProfileInterest_Serializer(serializers.ModelSerializer):

    class Meta : 
        model = ProfileInterest
        fields = ['interest']