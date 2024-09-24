from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


def RegisterView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response({'data':serializer.errors,
                                'message':'Something went wrong!'},
                                status=status.HTTP_400_BAD_REQUEST)
        
            serializer.save()

            return Response({'data':{},
                             'message':'Your Account has Created Successfully!'},
                             status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'data':{},
                            'message':'Something went wrong!'},
                            status=status.HTTP_400_BAD_REQUEST)