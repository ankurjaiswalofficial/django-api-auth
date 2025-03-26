import hashlib
import hmac
import time
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from hawk_auth.models import HawkCredential
from django.contrib.auth import get_user_model

User = get_user_model()

class HawkAuthentication(BaseAuthentication):

    def authenticate(self, request):
        hawk_header = request.headers.get('Authorization')
        if not hawk_header or not hawk_header.startswith('Hawk'):
            return None  # No Hawk header, move to the next authentication class

        try:
            # Extract Hawk parameters (e.g., Hawk id="user_id", ts="timestamp", mac="signature")
            params = dict(item.split('=') for item in hawk_header[5:].replace('"', '').split(', '))
            hawk_id = params.get('id')
            timestamp = params.get('ts')
            received_mac = params.get('mac')

            if not hawk_id or not timestamp or not received_mac:
                raise AuthenticationFailed('Invalid Hawk header format')

            # Validate timestamp (allow a 5-minute window)
            current_time = int(time.time())
            if abs(current_time - int(timestamp)) > 300:
                raise AuthenticationFailed('Hawk token expired')

            # Retrieve the user and secret key
            try:
                credential = HawkCredential.objects.get(hawk_id=hawk_id)
                user = credential.user
            except HawkCredential.DoesNotExist:
                raise AuthenticationFailed('Invalid Hawk credentials')

            secret_key = credential.secret_key

            # Compute expected HMAC
            expected_mac = hmac.new(
                secret_key.encode(),
                f"{hawk_id}{timestamp}".encode(),
                hashlib.sha256
            ).hexdigest()

            # Compare received and expected MAC securely
            if not hmac.compare_digest(received_mac, expected_mac):
                raise AuthenticationFailed('Invalid Hawk token')

            return (user, None)

        except Exception:
            raise AuthenticationFailed('Malformed Hawk header')

    @staticmethod
    def generate_hawk_token(user):
        """Generate a valid Hawk token for a user."""
        try:
            credential = HawkCredential.objects.get(user=user)
        except HawkCredential.DoesNotExist:
            raise AuthenticationFailed('Hawk credentials not found for user')

        timestamp = str(int(time.time()))
        mac = hmac.new(
            credential.secret_key.encode(),
            f"{credential.hawk_id}{timestamp}".encode(),
            hashlib.sha256
        ).hexdigest()

        return f'Hawk id="{credential.hawk_id}", ts="{timestamp}", mac="{mac}"'
