from django.urls import path
from .views import CreatePlayerView, DeletePlayerView, UpdatePlayerView, ListPlayersView


urlpatterns = [
    path('players/create/', CreatePlayerView.as_view(), name='create-player'),
    path('players/<uuid:pk>/delete/', DeletePlayerView.as_view(), name='delete-player'),
    path('players/<uuid:pk>/update/', UpdatePlayerView.as_view(), name='update-player'),
    path('players/', ListPlayersView.as_view(), name='list-players'),
]