from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    facebook = models.CharField(max_length=100)
    facebook_link = models.URLField(null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
