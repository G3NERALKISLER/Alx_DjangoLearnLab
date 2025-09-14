# bookshelf/management/commands/setup_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Set up default groups and permissions"

    def handle(self, *args, **kwargs):
        permissions = Permission.objects.filter(content_type__app_label="bookshelf", content_type__model="book")

        # Define groups and their permissions
        group_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                perm = permissions.get(codename=perm_codename)
                group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully"))
