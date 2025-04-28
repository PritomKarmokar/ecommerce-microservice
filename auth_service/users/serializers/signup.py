from rest_framework import serializers

from users.models import User

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')

        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise serializers.ValidationError("Following email address already exists. Please login instead.")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user