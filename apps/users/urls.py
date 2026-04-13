from django.urls import path
from .import views
from .views import RegisterUserAPIView,admin_only

urlpatterns = [
		path('register/',RegisterUserAPIView.as_view()),
		path('admin_only/',admin_only),
	]
