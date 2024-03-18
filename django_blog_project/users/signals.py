from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile
from django.core.signals import setting_changed,request_finished

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        p1=profile.objects.create(user=instance)
        p1.save()

@receiver(request_finished)
def request_handler(sender,**kwargs):
    print('Request Detected-------------')




