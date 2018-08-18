import shortuuid 

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify

from florists.models import Client

class Filters(models.Model):
    text = models.CharField("Text", max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete="CASCADE")

class BouquetPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=3)

# Create your models here.
class Bouquet(models.Model):
    cli = models.ForeignKey(Client, on_delete="CASCADE")
    name = models.CharField("Name", max_length=300) 
    description = models.CharField("Description", max_length=600) 
    size = models.IntegerField(default=5)
    upsize = models.IntegerField(default=5)
    price = models.DecimalField('Cost', max_digits=5, decimal_places=2, blank=True, null=True)
    upprice = models.DecimalField('Cost', max_digits=5, decimal_places=2, blank=True, null=True)
    max_qty = models.IntegerField(default=0)
    filters = models.ManyToManyField(Filters)
    images = ArrayField(models.URLField(), default=[])
    uuid = models.CharField("UUID", max_length=50, blank=True, null=True)
    status = models.IntegerField(default=1)
    objects = models.Manager()
    pub_objects = BouquetPublishedManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = shortuuid.uuid()

        super(Bouquet, self).save(*args, **kwargs)

    @property
    def slug_name(self):
        return slugify(self.name)

    @property
    def upsize_diff(self):
        return self.upprice - self.price