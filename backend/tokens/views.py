from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Token
from .serializers import TokenSerializer


class CreateTokenView(APIView):
    def post(self, request):
        origin_url = request.META.get('HTTP_REFERER')
        expected_url = 'http://localhost:3000/'
        # expected_url = ''

        if origin_url == expected_url:
            token = Token()
            token.save()
            serializer = TokenSerializer(token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid request origin'}, status=status.HTTP_403_FORBIDDEN)


def check_token(token_to_check):
    try:
        token = Token.objects.get(token=token_to_check)
        if token.active and not token.used:
            token.delete()
            return True
        else:
            token.delete()
            return False
    except Token.DoesNotExist:
        return False
