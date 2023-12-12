from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from emr.users.models import User as UserType, Profile


User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer[UserType]):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["username", "name", 'phone', 'email', 'created_at', 'profile']
    def get_profile(self, obj):
        profile = None
        try:
            profile = ProfileSerializer(obj.profile).data
        except ObjectDoesNotExist as e:
            pass
        return profile
       

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff

        return token