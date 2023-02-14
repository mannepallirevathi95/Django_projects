from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# a function to build profile with multiple parameters
# we have to powerup this function when user is created
# sender:sends signals ; instance:being saved ; created:user created or not- boolean values
@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
