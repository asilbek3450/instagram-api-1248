from django.shortcuts import render
from rest_framework import permissions

from .models import User, UserConfirmation
from .serializers import SignUpSerializer
from rest_framework.generics import CreateAPIView


# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer
