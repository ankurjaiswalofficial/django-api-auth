from django.urls import path
from .views import HawkAuthView

urlpatterns = [
    path('hawk-auth/', HawkAuthView.as_view(), name='hawk_auth'),
]
