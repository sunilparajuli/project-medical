import os
import requests
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File
from django.conf import settings
from PIL import Image
from faker import Faker
from emr.users.models import Profile, Role
from django.contrib.auth.hashers import make_password

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Create fake users, profiles, and roles for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating fake users, profiles, and roles...'))

        # Create roles
        admin_role, _ = Role.objects.get_or_create(name='admin')
        user_role, _ = Role.objects.get_or_create(name='user')

        # Create the profile_photos directory if it doesn't exist
        photo_directory = os.path.join(settings.MEDIA_ROOT, 'profile_photos')
        os.makedirs(photo_directory, exist_ok=True)

        for _ in range(10):  # Change 10 to the desired number of fake users
            username = fake.user_name()
            email = fake.email()
            password = make_password('test123')
            name = fake.name()
            

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                name=name
            )

            # Create a fake profile
            profile = Profile.objects.create(user=user)
            profile.phone = fake.phone_number()
            profile.address = fake.address()
            profile.role_id = fake.random_element([admin_role.id, user_role.id])

            # Download a fake photo from the internet
            photo_url = 'https://i.pngimg.me/thumb/f/720/m2i8Z5H7Z5d3Z5K9.jpg'
            response = requests.get(photo_url, stream=True)
            response.raise_for_status()

            # Save the photo to the profile
            photo_path = os.path.join(photo_directory, f'{user.username}.png')
            with open(photo_path, 'wb') as photo_file:
                for chunk in response.iter_content(chunk_size=8192):
                    photo_file.write(chunk)

            # Open the image using Pillow
            img = Image.open(photo_path)

            # Resize the image to 150x150
            img = img.resize((150, 150))

            # Save the resized image
            img.save(photo_path)

            profile.photo.save(f'profile_photos/{user.username}.png', File(open(photo_path, 'rb')))
            profile.save()

        self.stdout.write(self.style.SUCCESS('Fake users, profiles, and roles created successfully!'))
