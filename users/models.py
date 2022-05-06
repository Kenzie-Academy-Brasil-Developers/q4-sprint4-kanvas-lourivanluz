from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):

    uuid            = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    is_admin        = models.BooleanField(default=False)
    email           = models.EmailField(unique=True,max_length=125)
    username        = models.CharField(max_length=150,null=True)
    first_name      = models.CharField(max_length=80)
    last_name       = models.CharField(max_length=80)

    address         = models.ForeignKey('addresses.Addresses',on_delete=models.CASCADE, related_name='users',null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []




