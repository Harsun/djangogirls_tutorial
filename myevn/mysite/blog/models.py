from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.user')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())
    publis_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publis_date= timezone.now()
        self.save()
    def __str__(self):
        return self.baslik