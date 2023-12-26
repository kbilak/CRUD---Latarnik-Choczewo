from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from tokens.models import Token
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# Function to check if a token is valid and active
def check_token(token_to_check):
    try:
        # Try to get the token from the database
        token = Token.objects.get(token=token_to_check)
        if token.active:
            # If the token is active, delete it and return True
            token.delete()
            return True
        else:
            # If the token is not active, delete it and return False
            token.delete()
            return False
    except Token.DoesNotExist:
        # If the token does not exist, return False
        return False
    

# API view to create a new user
class CreateUserView(APIView):
    def post(self, request):
        # Get the token from the Authorization header
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        # If the token is not valid, return an error response
        if token_to_check and not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Invalid or expired token'}, status=status.HTTP_403_FORBIDDEN)

        # Get the email and password from the request data
        user_email = request.data.get('email')
        user_password = request.data.get('password')

        # Prepare the user data for serialization
        user_data = {
            'email': user_email,
            'password': user_password 
        }

        # Hash the password before storing it
        if 'password' in user_data:
            user_data['password_hash'] = make_password(user_data['password'])

        # Serialize the user data
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            # If the serialized data is valid, save it and return a success response
            serializer.save()
            return Response({'status': 0}, status=status.HTTP_201_CREATED)
        else:
            # If the serialized data is not valid, return an error response
            return Response({'status': 1, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# API view to log in a user
class LoginUserView(APIView):
    def post(self, request):
        # Get the token from the Authorization header
        token_to_check = None
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith('Bearer '):
            token_to_check = auth_header.split(' ')[1]

        # If the token is not valid, return an error response
        if token_to_check and not check_token(token_to_check):
            return Response({'status': 1, 'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        # Get the email and password from the request data
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate the email
        try:
            validate_email(email)
        except ValidationError:
            return Response({'status': 1, 'error': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the password
        if not password:
            return Response({'status': 1, 'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Try to get the user from the database
            user = User.objects.get(email=email)
            if check_password(password, user.password_hash):
                # If the password is correct, return a success response
                return Response({'status': 0, 'user': UserLoginSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                # If the password is incorrect, return an error response
                return Response({'status': 1, 'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            # If the user does not exist, return an error response
            return Response({'status': 1, 'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        