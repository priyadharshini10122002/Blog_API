from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data['username']).exists():
            raise  serializers.ValidationError('Username is Already Taken !')
        
        return data
