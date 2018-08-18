from django.contrib.auth.models import User
from django.db import models

from florists.models import Client

# Create your models here.
class FProfile(models.Model):
 	user = models.OneToOneField(User, related_name="fprofile", on_delete="CASCADE")
 	cli = models.ForeignKey(Client, on_delete="CASCADE")