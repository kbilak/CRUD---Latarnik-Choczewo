from django.urls import path
from .views import CreatePlayerView, DeletePlayerView, UpdatePlayerView, ListPlayersView, image_upload_view


urlpatterns = [
    path('create/', CreatePlayerView.as_view(), name='create-player'),
    path('<uuid:pk>/delete/', DeletePlayerView.as_view(), name='delete-player'),
    path('<uuid:pk>/update/', UpdatePlayerView.as_view(), name='update-player'),
    path('players/', ListPlayersView.as_view(), name='players-list'),
    path('image/', image_upload_view, name='player-image'),
]
