from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from users.serializers import LoginSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = authenticate(email=email, password=password)
            if user:
                user.last_login = timezone.now()
                user.save()
                refresh = RefreshToken.for_user(user)
                response = {
                    "message": f"{user.get_username()} logged in successfully.",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                }
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response = {
                    "message": "Invalid Credentials. Please try again.",
                }
                Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)