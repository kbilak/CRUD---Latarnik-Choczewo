from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Translations(APIView):
    def get(self, request, format=None):
        
        translations = [
            {
                'language': 'pl',
                'translations': [
                    {
                        'code': 'auth.login',
                        'translation': 'Logowanie'
                    },
                    {
                        'code': 'auth.sign_up',
                        'translation': 'Rejestracja'
                    },
                ]
            },
            {
                'language': 'en',
                'translations': [
                    {
                        'code': 'auth.login',
                        'translation': 'Login'
                    },
                    {
                        'code': 'auth.sign_up',
                        'translation': 'Sign Up'
                    },
                ]
            },
        ]

        return Response(translations)