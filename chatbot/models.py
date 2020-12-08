from django.db import models

# Create your models here.


class Question(models.Model):
    mid = models.CharField(max_length=4)
    msg = models.CharField(max_length=4096)

    def __str__(self):
        return {'mid':self.mid, 'msg':self.msg}
