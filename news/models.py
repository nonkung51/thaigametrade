from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class News(models.Model):
    time = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=600)

    def __str__(self):
        return str(self.text[:20])

class GameRequest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')
