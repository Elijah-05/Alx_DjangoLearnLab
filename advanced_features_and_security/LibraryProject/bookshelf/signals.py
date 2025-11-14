from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # only run for this app
    if sender.label != "bookshelf":
        return

    Permission = apps.get_model('auth', 'Permission')
    # permission codenames we defined on Book model and CustomUser
    perms = {
        "can_view": Permission.objects.filter(codename="can_view"),
        "can_create": Permission.objects.filter(codename="can_create"),
        "can_edit": Permission.objects.filter(codename="can_edit"),
        "can_delete": Permission.objects.filter(codename="can_delete"),
    }

    groups = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perm_keys in groups.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        # clear and set to ensure idempotence
        group.permissions.clear()
        for pk in perm_keys:
            for p in perms.get(pk, []):
                group.permissions.add(p)
        group.save()