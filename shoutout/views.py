from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.parsers import FormParser, JSONParser

from .models import organization, user, shoutout
from .serializers import OrganizationSerializer, UserSerializer, ShoutoutSerializer
from rest_framework import generics

import json
import os


def index(request):
    return HttpResponse("Hello  World!", status=200)


class OrganizationList(generics.ListCreateAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class UserList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class ShoutoutList(generics.ListCreateAPIView):
    queryset = shoutout.objects.all()
    serializer_class = ShoutoutSerializer


class ShoutoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = shoutout.objects.all()
    serializer_class = ShoutoutSerializer
