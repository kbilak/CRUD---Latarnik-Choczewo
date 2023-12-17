from django.urls import path
from .views import *


urlpatterns = [
    path('translations/', Translations.as_view(), name='get-translations'),
]
