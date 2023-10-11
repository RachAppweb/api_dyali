from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions,generics,status
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
# Create your views here.

class UserView(generics.CreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
        
       

    def create(self, request,*args,**kwargs):
 
        try:
                 password=self.request.data['password']  
            
        except (KeyError, AttributeError,AssertionError,ArithmeticError):
                print('its key error')
                raise ValidationError({"error":"you may missed something"})
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
                serializer.save(password=make_password(password))  
            
        except (KeyError, AttributeError,AssertionError,ArithmeticError):
                print('its key error')
                raise ValidationError({"error":"error accured"})
        return Response({"details":serializer.data})
             
        
    def get(self, request):
        try:
            user=UserSerializer(request.user)
            return Response(user.data)
        except (AttributeError,AssertionError,ArithmeticError):
            raise ValidationError({"error":"something bad happened "})