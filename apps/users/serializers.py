from rest_framework import serializers
#from .models import UserProfile
from .models import User
from django.contrib.auth.hashers import make_password

#class UserProfileSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.ModelSerializer):
	class Meta:
#		model = UserProfile
		model = User
		#fields = '__all__'
		fields = ['id','username','email','password','role']
		extra_kwargs = {
			'password':{'write_only':True}
		}

	def create(self,validated_data):
		#validated_data['password'] = make_password(validated_data['password'])
		user = User.objects.create_user(**validated_data)     #create_user() handles  hashing automatically
		#return super().create(validated_data)
		return user
