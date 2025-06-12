from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import os

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GoogleLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            code = request.data.get('code')
            if not code:
                return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Exchange code for tokens using GoogleOAuth2Adapter
            adapter = GoogleOAuth2Adapter()
            client = OAuth2Client(
                adapter.client_id,
                adapter.client_secret,
                adapter.access_token_method,
                adapter.access_token_url,
                adapter.callback_url,
                adapter.scope
            )
            token = client.get_access_token(code)

            # Get user info from Google
            user_info = adapter.get_user_info(token)
            email = user_info.get('email')
            
            if not email:
                return Response({'error': 'No email provided by Google'}, status=status.HTTP_400_BAD_REQUEST)

            # Get or create user
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Create new user
                username = email.split('@')[0]
                user = User.objects.create_user(
                    email=email,
                    username=username,
                    first_name=user_info.get('given_name', ''),
                    last_name=user_info.get('family_name', ''),
                    is_verified=True  # Google accounts are verified
                )

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserProfileSerializer(user).data
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
