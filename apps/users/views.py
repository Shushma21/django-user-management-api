from  rest_framework.generics import CreateAPIView
from .models import User
from .serializers import  UserSerializer,RegisterSerializer
from .permissions import IsAdminUserRole
from  rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

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
	filter_backends = [DjangoFilterBackend,SearchFilter]
	filterset_fields = ['role']
	search_fields = ['username','email']
	
	def get_permissions(self):
		if self.action in['list','destroy']:
			return[IsAuthenticated(),IsAdminUserRole()]
		return [IsAuthenticated()]

	def get_queryset(self):
		if self.request.user.role == 'admin':
			return User.objects.all()
		return User.objects.filter(id=self.request.user.id)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		page 	= self.paginate_queryset(queryset)

		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response({"status": "success", "data": serializer.data})

		serializer = self.get_serializer(queryset, many=True)
		return Response({"status": "success","data": serializer.data})
