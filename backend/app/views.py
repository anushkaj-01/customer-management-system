from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['POST','GET'])
def addContact(request):
    if request.method == 'POST':
        data = request.data
        serializer = customerSerializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        customers = Customerinfo.objects.all()
        
        for customer in customers:
            print(customer.name)
            serializer = customerSerializer(data=customer, many=True)
            if(serializer.is_valid()):
                list = [serializer.data]
                return Response(list)
            return Response(serializer.errors)

    else: 
        return Response("invalid")   
    