from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog
from django.db.models import Q
# Create your views here.

class BlogView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        try:
              blog= Blog.objects.filter(user=request.user)
              if request.GET.get('search'):
                search=request.GET.get('search')
                blog=blog.filter(Q(title__icontains=search) |  Q(blog_text__icontains=search))

              serializer=BlogSerializer(blog,many=True)
              return Response({'data':serializer.data,
                             'message':'Blogs fetched Successfully!'},
                             status=status.HTTP_201_CREATED)
        
        except Exception as e:
            
            print(e)
            return Response({'data':{},
                            'message':'Something went wrong!'},
                            status=status.HTTP_400_BAD_REQUEST)
        




    def post(self, request):
        try:
            data=request.data
            print(request.user)
            data['user']=request.user.id
            serializer=BlogSerializer(data=data)

            if not   serializer.is_valid():
                     return Response({'data':serializer.errors,
                                'message':'Something went wrong!'},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response({'data':serializer.data,
                             'message':'Blog has been  Created Successfully!'},
                             status=status.HTTP_201_CREATED)
        
        
        except Exception as e:
            
            print(e)
            return Response({'data':{},
                            'message':'Something went wrong!'},
                            status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        try:
            data=request.data
            print(request.user)
            blog=Blog.objects.filter(uid = data.get('uid'))

            if not blog.exists:
                return Response({'data':{},
                            'message':'No Blog post exitst for this uid!'},
                            status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                
                return Response({'data':{},
                            'message':'You are not allowed to perform this operation to this Blog!'},
                            status=status.HTTP_400_BAD_REQUEST)

            serializer=BlogSerializer(blog[0],data=data,partial=True)

            
            if not serializer.is_valid():
                     return Response({'data':serializer.errors,
                                'message':'Something went wrong Serializer not Valid!'},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response({'data':serializer.data,
                             'message':'Blog has been Updated Successfully!'},
                             status=status.HTTP_201_CREATED)
                
        except Exception as e:
            
            print(e)
            return Response({'data':{},
                            'message':'Something went wrong!'},
                            status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request):
        try:
            data=request.data
            print(request.user)
            blog=Blog.objects.filter(uid = data.get('uid'))

            if not blog.exists:
                return Response({'data':{},
                            'message':'No Blog post exitst for this uid!'},
                            status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                
                return Response({'data':{},
                            'message':'You are not allowed to perform this operation to this Blog!'},
                            status=status.HTTP_400_BAD_REQUEST)

            blog[0].delete()
            
            return Response({'data':{},
                             'message':'Blog has been Deleted Successfully!'},
                             status=status.HTTP_201_CREATED)
        except Exception as e:
            
            print(e)
            return Response({'data':{},
                            'message':'Something went wrong!'},
                            status=status.HTTP_400_BAD_REQUEST)
        
    
        


