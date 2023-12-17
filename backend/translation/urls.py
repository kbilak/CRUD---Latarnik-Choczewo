from django.urls import path
from .views import *


urlpatterns = [
    path('translations/', LanguageListAPIView.as_view(), name='get-translations'),
]
