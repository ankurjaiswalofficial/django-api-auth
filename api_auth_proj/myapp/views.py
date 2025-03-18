from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CustomAuthToken(ObtainAuthToken):
    """
    Sample Request:
    POST /api-token-auth/ HTTP/1.1
    Host: example.com
    Content-Type: application/json
    {
        "username": "user",
        "password": "pass"
    }

    Sample Response (Token Created):
    HTTP/1.1 200 OK
    {
        "token": "abc123",
        "user_id": 1,
        "email": "user@example.com"
    }

    Sample Response (Token Not Created):
    HTTP/1.1 200 OK
    {
        "token": "",
        "user_id": 1,
        "email": "user@example.com"
    }
    """

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response({
            'error': 'Invalid credentials'
        })
