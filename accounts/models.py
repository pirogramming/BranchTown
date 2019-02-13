from django.db import models
from django.conf import settings
from tag.models import Tag


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag)
    occupation = models.CharField(max_length=20)
