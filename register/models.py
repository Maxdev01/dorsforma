from django.db import models

# Create your models here.


class Regist(models.Model):


    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tel = models.IntegerField()
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name
