from .tasks import convert480p
from .models import Film
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
import os

@receiver(post_save, sender=Film)
def video_post_save(sender, instance, created, **kwargs):
    if(created):
        print('Video created')
        video_path_as_str = str(instance.video_file)
        modified_video_path = '.' + video_path_as_str[6:]
        convert480p(modified_video_path)


@receiver(post_delete, sender=Film)
def video_delete_post(sender, instance, **kwargs):
    print('Video deleted successfully')
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)

