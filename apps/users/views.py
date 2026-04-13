from  rest_framework.generics import CreateAPIView
from .models import UserProfile, User
from .serializers import  UserSerializer
from .permissions import IsAdminUserRole
from  rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

class RegisterUserAPIView(CreateAPIView):
	#queryset = UserProfile.objects.all()
	queryset = User.objects.all()
	#serializer_class = UserProfileSerializer
	serializer_class = UserSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUserRole])
def admin_only(request):
	return Response({"message":"Only admin can access this"})
