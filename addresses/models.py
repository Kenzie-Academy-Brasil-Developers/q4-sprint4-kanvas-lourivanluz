from tkinter import CASCADE
from django.db import models
from uuid import uuid4


class Addresses(models.Model):

    uuid            = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    street          = models.CharField(max_length=255,null=False)
    house_number    = models.IntegerField(null=False)
    city            = models.CharField(max_length=255,null=False)
    state           = models.CharField(max_length=255,null=False)
    zip_code        = models.CharField(max_length=255,null=False)
    country         = models.CharField(max_length=255,null=False)
