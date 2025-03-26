from django.http import HttpResponseForbidden
from django.conf import settings


ALLOWED_ORIGINS = getattr(settings, "SECURE_ALLOWED_ORIGINS", [])
ALLOWED_IPS = getattr(settings, "SECURE_ALLOWED_IPS", [])
ENABLE_IP_CHECK = getattr(settings, "SECURE_ENABLE_IP_CHECK", False)

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get("REMOTE_ADDR")

def secure_api_access(get_response):
    def middleware(request):
        origin = request.META.get("HTTP_ORIGIN")
        referer = request.META.get("HTTP_REFERER")

        origin_allowed = any(
            origin and origin.startswith(allowed) for allowed in ALLOWED_ORIGINS
        )
        referer_allowed = any(
            referer and referer.startswith(allowed) for allowed in ALLOWED_ORIGINS
        )

        ip_allowed = True
        if ENABLE_IP_CHECK:
            client_ip = get_client_ip(request)
            ip_allowed = client_ip in ALLOWED_IPS

        if not (origin_allowed or referer_allowed) or not ip_allowed:
            return HttpResponseForbidden("Access Denied: Unauthorized origin or IP")

        return get_response(request)
    return middleware
