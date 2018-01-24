from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    # If the description textfield is set to null=true, than the description field can be empty
    description = models.TextField(default='description default text')
    # model has a field called name, the unicode returns the profile name(self.name)
    

    def __unicode__(self):
        return self.name
