from .models import Choice
from rest_framework import serializers


class Choice_Serializer(serializers.ModelSerializer):

    # In order to include 'votes' method define in models
    # Because it's not a model field, it needs to be added explicitly to the serializer class
    
    votes = serializers.ReadOnlyField()  
    class Meta:
        model = Choice
        fields = "__all__"