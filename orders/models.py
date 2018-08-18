from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from products.models import Bouquet

# Create your models here.
class Cart(models.Model):
	cdate = models.DateField()
	data = JSONField()
	user = models.ForeignKey(User, on_delete='CASCADE')
