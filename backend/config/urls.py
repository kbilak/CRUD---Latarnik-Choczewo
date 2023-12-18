from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('translation/', include('translation.urls')),
    path('token/', include('tokens.urls')),
    path('auth/', include('accounts.urls')),
]
