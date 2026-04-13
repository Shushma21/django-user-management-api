from  rest_framework.generics import CreateAPIView
from .models import User
from .serializers import  UserSerializer,RegisterSerializer
from .permissions import IsAdminUserRole
from  rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

class RegisterUserAPIView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer

	def create(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response({"status":"success","data":serializer.data},status=status.HTTP_201_CREATED)
		return Response({"status":"error","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUserRole])
def admin_only(request):
        return Response({"status":"success","message":"Only admin can access this"})

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUserRole])
def current_user(request):
	serializer = UserSerializer(request.user)
	return Response({"status":"success","data":serializer.data})


class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
	def get_permissions(self):
		if self.action in['list','destroy']:
			return[IsAuthenticated(),IsAdminUserRole()]
		return [IsAuthenticated()]

	def get_queryset(self):
		if self.request.user.role == 'admin':
			return User.objects.all()
		return User.objects.filter(id=self.request.user.id)

