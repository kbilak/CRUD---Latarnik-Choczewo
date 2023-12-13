from django.urls import path
from .views import *


urlpatterns = [
    path('pl/', TranslationsPL.as_view(), name='create-user'),
]
