import shortuuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill

STAT_CHOICES = (
		(1, 'Live'),
		(2, 'Offline'),
		(3, 'Deactivated'),
		(4, 'Signup'),
	)
# Create your models here.

def gen_file_name(instance, filename):
    return '%s/%s' % (instance.uuid, filename)


class Client(models.Model):
	bname = models.CharField("Registered Business Name", max_length=400)
	con_name = models.CharField("Name of Contact", max_length=300)
	con_email = models.CharField("Contact No.", max_length=300)
	status = models.IntegerField(choices=STAT_CHOICES, default=4)

	address = models.TextField(blank=True, null=True)
	acra = models.CharField("ACRA Number", max_length=50, blank=True, null=True)
	con_number = models.IntegerField(blank=True, null=True)

	uuid = models.CharField("Shortuuid", max_length=50, blank=True, null=True)
	days = ArrayField(models.CharField(max_length=10),default=[])
	hours = ArrayField(models.IntegerField(), default=[])
	questions = ArrayField(models.TextField(), default=[])

	logo = ProcessedImageField(upload_to=gen_file_name,
                                           processors=[ResizeToFit(400, 400)],
                                           format='PNG',
                                           options={'quality': 90}, blank=True, null=True)

	banner = ProcessedImageField(upload_to=gen_file_name,
                                           processors=[ResizeToFill(1920, 1280)],
                                           format='PNG',
                                           options={'quality': 90}, blank=True, null=True)


	def save(self, *args, **kwargs):
   		if not self.id:
   			self.uuid = shortuuid.uuid()
   		super(Client, self).save(*args, **kwargs)