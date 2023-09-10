from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from .producer import ProducerUserCreated
from rest_framework.response import Response
from rest_framework import status
import json

# Initialize producer 
producerUserCreated=ProducerUserCreated()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    #permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Procuder 
        producerUserCreated.publish("user_created_method",json.dumps(serializer.data))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)