# post_save/delete froom signals implies that these signals are sent by django 
# to the entire application after a model instance is save or deleted. 
# To receive these signals we need receiver from dispatch
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem  # We listen for signals on this model...


@receiver(post_save, sender=OrderLineItem)
# Special type of fucntion that will handle signals from the post_save event
def update_on_save(sender, instance, created, **kwards):
    '''
    Update order total on lineitem update/create
    '''
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
# Special type of fucntion that will handle signals from the post_delete event
def update_on_delete(sender, instance, **kwards):
    '''
    Update order total on lineitem delete
    '''
    instance.order.update_total()
