from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from users.serializers import LogoutSerializer

class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                refresh = serializer.validated_data.get("refresh_token")
                token = RefreshToken(refresh)
                token.blacklist()

                response = {
                    "message": "Logout Successful!"
                }
                return Response(data=response, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            response = {
                "message": "Invalid token..."
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

