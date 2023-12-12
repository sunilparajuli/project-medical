from django.contrib.auth.models import AbstractUser
from django.db  import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for emr.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    phone = models.CharField(_("Phone"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone = models.CharField(_("Phone"), max_length=255, blank=True)
    created_at = models.DateTimeField(_("Created At"), null=True, auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), null=True, auto_now=True)    

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Role(models.Model):
    name = models.CharField(_("Role Name"), max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(
        User,  # Replace 'YourAppName' with the actual name of your app
        on_delete=models.CASCADE,
        related_name='profile'
    )
    photo = models.ImageField(_("Profile Photo"), upload_to='profile_photos/', blank=True, null=True)
    address = models.TextField(_("Address"), blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}"