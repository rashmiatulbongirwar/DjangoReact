from django.shortcuts import render

from .serializers import UserInfoSerializer, OrgMemSerializer
from .models import UserInfo, OrgMem
from rest_framework import viewsets




class UserInfoViewSet(viewsets.ModelViewSet):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer

class OrgMemViewSet(viewsets.ModelViewSet):
	queryset = OrgMem.objects.all()
	serializer_class = OrgMemSerializer
