from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Player
from .serializers import PlayerSerializer
from tokens.models import Token


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
        token_to_check = request.data.get('token', '')

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
        token_to_check = request.data.get('token', '')

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
        token_to_check = request.data.get('token', '')

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
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    