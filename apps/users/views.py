from  rest_framework.generics import CreateAPIView
#from .models import UserProfile
from .models import User
#from .serializers import UserProfileSerializer
from .serializers import UserSerializer

class RegisterUserAPIView(CreateAPIView):
	#queryset = UserProfile.objects.all()
	queryset = User.objects.all()
	#serializer_class = UserProfileSerializer
	serializer_class = UserSerializer
