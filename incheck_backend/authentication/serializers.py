from rest_framework import serializers

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class AdminSignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, write_only=True)

    def validate_password(self, value):
        # Tu peux ajouter des validations supplémentaires sur le mot de passe si nécessaire
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value