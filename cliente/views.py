from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cliente.models import Cliente

from cliente.serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateClient(APIView):
    
    def post(self, request, format=None):
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListClient(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        cliente = Cliente.objects.all()
        serializer = ClientSerializer(cliente, many=True)
        return Response(serializer.data)
