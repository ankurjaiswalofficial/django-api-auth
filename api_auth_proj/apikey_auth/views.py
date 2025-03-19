from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import APIKey

class SampleAPIKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "API key authentication successful!"})

class APIKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the API key for the authenticated user
        api_key = APIKey.get_or_create_key(request.user)
        return Response({'api_key': api_key})

    def post(self, request):
        # Regenerate the API key for the authenticated user
        api_key = APIKey.get_or_create_key(request.user)
        api_key_obj = request.user.api_key
        api_key_obj.key = APIKey.generate_key()
        api_key_obj.save()
        return Response({'api_key': api_key_obj.key})
