from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.serializers import ProfileSerializer


class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        user = request.user
        serializer = self.serializer_class(instance=user)
        response = {
            "message": f"Profile information for, {user.username}",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        user = request.user
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Profile updated successfully.",
                "data":serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

