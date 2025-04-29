from rest_framework import serializers
from users.models import User

class ProfileSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%B %d, %Y at %I:%M %p", read_only=True)
    email = serializers.EmailField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']

# class ProfileUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username']