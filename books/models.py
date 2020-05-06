from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class issuebook(models.Model):
    username = models.CharField(max_length=255)
    clgid = models.IntegerField(default = 1)
    bookname = models.CharField(max_length=255)
    bookid = models.IntegerField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.bookname

class returnbook(models.Model):
    username = models.CharField(max_length=255)
    clgid = models.IntegerField()
    bookname = models.CharField(max_length=255)
    bookid = models.IntegerField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.bookname
