from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreatePlayerView.as_view(), name='create-player'),
    path('<uuid:pk>/delete/', DeletePlayerView.as_view(), name='delete-player'),
    path('<uuid:pk>/update/', UpdatePlayerView.as_view(), name='update-player'),
    path('players/', ListPlayersView.as_view(), name='players-list'),
    path('image/', image_upload_view, name='player-image'),
    path('coach/image/', image_upload_view_coach, name='coach-image'),
    path('coaches/', ListCoachesView.as_view(), name='coaches-list'),
    path('coach/create/', CreateCoachView.as_view(), name='create-coach'),
    path('coach/<uuid:pk>/delete/', DeleteCoachView.as_view(), name='delete-coach'),
    path('coach/<uuid:pk>/update/', UpdateCoachView.as_view(), name='update-coach'),
]
