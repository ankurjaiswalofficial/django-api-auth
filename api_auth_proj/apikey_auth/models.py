from django.db import models
from django.contrib.auth.models import User
import secrets

# Model to store API keys
class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='api_key')
    key = models.CharField(max_length=40, unique=True)

    @staticmethod
    def generate_key():
        return secrets.token_hex(20)

    @classmethod
    def get_or_create_key(cls, user):
        api_key, created = cls.objects.get_or_create(user=user)
        if created or not api_key.key:
            api_key.key = cls.generate_key()
            api_key.save()
        return api_key.key
