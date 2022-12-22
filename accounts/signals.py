from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.db.models import signals
from . models import User,UserProfile,UserManager

    # signals
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
           profile=UserProfile.objects.get(user=instance)
           profile.save()
        except:
            # create the userprofile if not exist
               profile=UserProfile.objects.get(user=instance)


    
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    pass

         


