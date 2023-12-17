from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *


class LanguageListAPIView(generics.ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.filter(active=True)
