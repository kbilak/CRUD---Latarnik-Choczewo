from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from tokens.models import Token
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password


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


class CreateUserView(APIView):
    def post(self, request):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        print(token_to_check)
        if token_to_check and not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        user_email = request.data.get('email')
        user_password = request.data.get('password')

        user_data = {
            'email': user_email,
            'password': user_password 
        }

        if 'password' in user_data:
            user_data['password_hash'] = make_password(user_data['password'])

        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 0}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    def post(self, request):
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        if token_to_check and not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password_hash):
                return Response({'status': 0, 'user': UserLoginSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 1, 'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            return Response({'status': 1, 'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
