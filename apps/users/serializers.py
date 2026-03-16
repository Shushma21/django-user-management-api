from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = '__all__'

	def create(self,validated_data):
		validated_data['password'] = make_password(validated_data['password'])
		return super().create(validated_data)
