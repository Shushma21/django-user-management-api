from django.urls import path,include
#from .import views
from rest_framework.routers import DefaultRouter
from .views import RegisterUserAPIView,UserViewSet,admin_only

router = DefaultRouter()
router.register(r'',UserViewSet)

urlpatterns = [
		path('register/',RegisterUserAPIView.as_view()),
		path('admin_only/',admin_only),
		path('',include(router.urls)),
	]
