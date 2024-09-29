from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise  serializers.ValidationError('Username is Already Taken !')
        return data
    

    def create(self,validated_data):
        user=User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],    
            username=validated_data['username'])
        
        user.set_password(validated_data['password'])
        user.save() 
        return validated_data


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):

        print(data['username'],User.objects.filter(username=data['username']))

        if not User.objects.filter(username=data['username']).exists():
            raise  serializers.ValidationError('Account Not Found !')
        return data
    
    def get_jwt_token(self,data):
        
        user=authenticate(username=data['username'],password=data['password'])

        if not user:
            return {'message':'Invalid Credentials' ,'data':{}}
        
        refresh=RefreshToken.for_user(user)
        return {'message':'Login Success!' ,'data':{'token':
     {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }   }}