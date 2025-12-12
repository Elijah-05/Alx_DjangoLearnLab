from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target):
    if recipient == actor:
        return  # Avoid self-notifications

    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_ct=ContentType.objects.get_for_model(target.__class__),
        target_id=target.id,
    )
