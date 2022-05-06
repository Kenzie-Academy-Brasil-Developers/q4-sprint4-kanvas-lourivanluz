from django.db import models
from uuid import uuid4


class Courses(models.Model):

    uuid            = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    name            = models.CharField(max_length=125,null=False,unique=True)
    demo_time       = models.TimeField(null=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    link_repo       = models.CharField(max_length=125)

    students        = models.ManyToManyField('users.Users',related_name='courses')
    instructor      = models.OneToOneField('users.Users',related_name='course',default=None,on_delete=models.CASCADE)