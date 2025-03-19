from django.urls import path
from .views import SampleAPIKeyView, APIKeyView

urlpatterns = [
    path('sample/', SampleAPIKeyView.as_view(), name='sample-api-key'),
    path('api-key/', APIKeyView.as_view(), name='api-key'),
]
