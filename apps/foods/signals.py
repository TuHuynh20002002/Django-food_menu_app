from .models import Item
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


@receiver(pre_save, sender=Item)
def set_created_at(sender, instance, **kwargs):
    if not instance.pk:
        instance.created_at = timezone.now()
