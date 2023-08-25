from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    pass


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    
   

    