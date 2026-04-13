from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

# For reading user data
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','email','role']

# For registration
class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','email','password','role']
		extra_kwargs = {
			'password':{'write_only':True}
		}
	
	def validate_email(self,value):
		if User.objects.filter(email=value).exists():
			raise serializers.ValidationError("Email already exists")
		if "@" not in value:
			raise serializers.ValidationError("Enter a valid email address")
		return value

	def validate_password(self,value):
		if len(value) < 6:
			raise serializers.ValidationError("Password must be atleast 6 characters")
		validate_password(value)
		return value

	def create(self,validated_data):
		user = User.objects.create_user(**validated_data)     #create_user() handles  hashing automatically
		return user
