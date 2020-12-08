from django.db import models

# Create your models here.


class Question(models.Model):
    mid = models.CharField(max_length=4)
    msg = models.CharField(max_length=4096)

    def __unicode__(self):
        return '{}'.format(self.description)
