from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserAPIView,UserViewSet,admin_only,current_user

router = DefaultRouter()
router.register(r'',UserViewSet)

urlpatterns = [
		path('register/',RegisterUserAPIView.as_view()),
		path('admin_only/',admin_only),
		path('me/',current_user),
		path('',include(router.urls)),
	]
