from django.db import models

# Create your models here.


class MediaDate(models.Model):
    class Meta:
        db_table='media_dict'
    filename = models.CharField(max_length=255,default=None)
    majortype= models.CharField(max_length=255,default=None)
    minortype = models.CharField(max_length=255,default=None)
    value = models.CharField(max_length=500,default=None)
    domain = models.CharField(max_length=200,default=None)












