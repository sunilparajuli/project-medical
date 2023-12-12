# your_app/management/commands/populate_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Populate users if database is empty (except superuser)'

    def handle(self, *args, **options):
        # Check if there are any users in the database (except superuser)
        if User.objects.filter(is_superuser=False).count() == 0:
            self.stdout.write(self.style.SUCCESS('Populating users...'))

            # Add your logic to create users here
            for i in range(100):
                User.objects.create_user(
                    username=f'user{i}',
                    password='password123',  # Change this to a secure password
                )

            self.stdout.write(self.style.SUCCESS('Users populated successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Users already exist. No need to populate.'))
