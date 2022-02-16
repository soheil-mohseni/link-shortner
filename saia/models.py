from django.db import models

# Create your models here.

class mysaia(models.Model):
    port1 = models.CharField(max_length= 1000)
    port2 = models.CharField(max_length= 1000)
    export = models.CharField(max_length= 1000)
    
