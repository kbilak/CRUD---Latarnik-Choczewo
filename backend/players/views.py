from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Player, Coach
from .serializers import PlayerSerializer, CoachSerializer
from tokens.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


def check_token(token_to_check):
    try:
        token = Token.objects.get(token=token_to_check)
        if token.active:
            token.delete()
            return True
        else:
            token.delete()
            return False
    except Token.DoesNotExist:
        return False


class CreatePlayerView(APIView):
    def post(self, request):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 0}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeletePlayerView(APIView):
    def delete(self, request, pk):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        try:
            player = Player.objects.get(pk=pk)
            player.delete()
            return Response({'status': 0, 'message': 'Player deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Player.DoesNotExist:
            return Response({'status': 1, 'error': 'Player does not exist'}, status=status.HTTP_404_NOT_FOUND)


class UpdatePlayerView(APIView):
    def put(self, request, pk):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({'status': 1, 'error': 'Player does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 0, 'message': 'Player updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListPlayersView(ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        referring_url = self.request.META.get('HTTP_REFERER')

        # specific_url = 'https://crud-latarnik-choczewo.vercel.app'
        specific_url = 'http://localhost:3000/'

        if referring_url == specific_url:
            return Player.objects.all()
        else:
            raise PermissionDenied("Access denied for this URL")


class ListCoachesView(ListAPIView):
    serializer_class = CoachSerializer

    def get_queryset(self):
        referring_url = self.request.META.get('HTTP_REFERER')

        # specific_url = 'https://crud-latarnik-choczewo.vercel.app'
        specific_url = 'http://localhost:3000/'

        if referring_url == specific_url:
            return Coach.objects.all()
        else:
            raise PermissionDenied("Access denied for this URL")


@csrf_exempt
def image_upload_view(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        if not check_token(token):
            return JsonResponse({'status': 1, 'error': 'Invalid or expired token'}, status=403)
        
        player_id = request.POST.get('playerId')
        player = get_object_or_404(Player, id=player_id)
        image_file = request.FILES.get('image')

        if image_file:
            player.image = image_file
            player.save()

            return JsonResponse({'status': 0, 'message': 'Image saved successfully'})

    return JsonResponse({'status': 1, 'error': 'Invalid request'}, status=400)


class CreateCoachView(APIView):
    def post(self, request):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 0}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCoachView(APIView):
    def delete(self, request, pk):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        try:
            coach = Coach.objects.get(pk=pk)
            coach.delete()
            return Response({'status': 0, 'message': 'Coach deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Coach.DoesNotExist:
            return Response({'status': 1, 'error': 'Coach does not exist'}, status=status.HTTP_404_NOT_FOUND)


class UpdateCoachView(APIView):
    def put(self, request, pk):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        try:
            coach = Coach.objects.get(pk=pk)
        except Coach.DoesNotExist:
            return Response({'status': 1, 'error': 'Coach does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CoachSerializer(coach, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 0, 'message': 'Coach updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
