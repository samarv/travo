from .models import organization
from .serializers import OrganizationSerializer
from rest_framework import generics


class OrganizationList(generics.ListCreateAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer
