from django.shortcuts import render
from users.models import CustomsUser as User
from users.serializers import UserListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
class UserList(APIView):
    
    def get(self,request):
        user = User.objects.all()
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data)
        
class UserList2(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer