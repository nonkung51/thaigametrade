from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from accounts.models import Profile

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    game = models.ForeignKey(Game, related_name='products')
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(Profile, related_name='products')

    def __str__(self):
        return str(self.game) + " " + str(self.price) + " " + str(self.seller)

    def get_absolute_url(self):
        return reverse("game:product",kwargs={'pk':self.pk})
