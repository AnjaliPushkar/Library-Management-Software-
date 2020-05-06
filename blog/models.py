from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class create(models.Model):
    title = models.CharField(max_length=255)
    bookno = models.IntegerField()
    pub_date = models.DateTimeField()
    body = models.TextField()
    no = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
