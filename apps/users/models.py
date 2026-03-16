from django.db import models

from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255,default = "null")
    role = models.CharField(max_length=20, default="user")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
