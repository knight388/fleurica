from django.db import models

from datetime import datetime

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

def gen_file_name(instance, filename):
    now = datetime.now()
    ext = filename.split('.')[-1]
    filename = instance.uuid + '.' + ext
    cli = instance.client.uuid
    
    return '%s/%s/%s/%s' % (cli, str(now.year), str(now.month), filename)

def gen_file_name_thumb(instance, filename):
    now = datetime.now()
    uuid = instance.uuid
    cli = instance.client.uuid
    return '%s/%s/%s/%s_thumb.png' % (cli, str(now.year), str(now.month), uuid)

# Create your models here.
class FImage(models.Model):
    client = models.ForeignKey('florists.Client', blank=True, null=True, on_delete="CASCADE")
    uuid = models.CharField("UUID", max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to=gen_file_name, blank=True, null=True)
    img_main = ProcessedImageField(upload_to=gen_file_name_thumb,
                               processors=[ResizeToFit(800, 800)],
                               format='PNG',
                               options={'quality': 100}, blank=True, null=True)
    img_thumb = ImageSpecField(source='img_main',
                               processors=[ResizeToFit(300, 300)],
                               format='PNG',
                               options={'quality': 100})