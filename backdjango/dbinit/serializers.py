from rest_framework import serializers
from .models import UserInfo, OrgMem
#from rest_framework.validators import UniqueValidator
#from django.contrib.auth.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserInfo
		fields = ('id', 'uname','fname', 'mname','lname','pwd','address','city','state','zipcode')


class OrgMemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrgMem
		fields = ('id', 'orgname','desc', 'address','city','zipcode','state','phone','upload')
