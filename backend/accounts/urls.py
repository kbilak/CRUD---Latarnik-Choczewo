from django.urls import path
from .views import *


urlpatterns = [
    path('sign-up/', CreateUserView.as_view(), name='create-user'),
    path('login/', LoginUserView.as_view(), name='login-user'),
]
