from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
