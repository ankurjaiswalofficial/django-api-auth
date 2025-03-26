from django.db import models
from django.contrib.auth.models import User

class HawkCredential(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hawk_credential')
    secret_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HawkCredential for {self.user.username}"
