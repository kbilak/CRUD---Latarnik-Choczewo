from django.urls import path
from .views import CreateTokenView


urlpatterns = [
    path('get/', CreateTokenView.as_view(), name='get-token'),
]
