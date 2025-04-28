from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from users.serializers import SignUpSerializer

class SignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            username = serializer.validated_data.get('username')
            response = {
                "message": f"{username}, your account has been created successfully.",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)