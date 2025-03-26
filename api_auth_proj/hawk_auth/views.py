from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from mohawk import Receiver
from mohawk.exc import HawkFail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import HawkCredential
import uuid
import secrets

class HawkAuthView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Authenticate the request using Hawk.
        """
        try:
            receiver = Receiver(
                lambda key_id: self.get_hawk_credentials(key_id),
                request.META.get('HTTP_AUTHORIZATION', ''),
                request.build_absolute_uri(),
                request.method,
                content=request.body,
                content_type=request.META.get('CONTENT_TYPE', '')
            )
            return JsonResponse({"message": "Hawk authentication successful"}, status=200)
        except HawkFail as e:
            return JsonResponse({"error": str(e)}, status=401)

    def get(self, request, *args, **kwargs):
        """
        Generate and return Hawk credentials (key and id).
        """
        hawk_id = str(uuid.uuid4())
        hawk_key = secrets.token_urlsafe(32)
        HawkCredential.objects.create(
            user=request.user,
            secret_key=hawk_key
        )
        return JsonResponse({"id": hawk_id, "key": hawk_key}, status=200)

    @staticmethod
    def get_hawk_credentials(key_id):
        """
        Retrieve Hawk credentials for the given key_id.
        """
        try:
            credential = HawkCredential.objects.get(user__username=key_id)
            return {"id": key_id, "key": credential.secret_key, "algorithm": "sha256"}
        except HawkCredential.DoesNotExist:
            raise HawkFail("Invalid Hawk credentials")
