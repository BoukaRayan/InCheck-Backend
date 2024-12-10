from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import AdminLoginSerializer
from .serializers import AdminSignupSerializer

class AdminLoginView(APIView):
    permission_classes = []  # Accessible publiquement

    def post(self, request):
        # Validation des données avec le serializer
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Authentification de l'utilisateur
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        # Génération des tokens JWT
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(tokens, status=status.HTTP_200_OK)


class AdminSignupView(APIView):
    permission_classes = []  # Accessible publiquement

    def post(self, request):
        # Validation des données avec le serializer
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Vérification si le username existe déjà
            if get_user_model().objects.filter(username=username).exists():
                return Response(
                    {"error": "Username already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Création de l'utilisateur
            user = get_user_model().objects.create_user(username=username, password=password)

            return Response(
                {"message": "User created successfully", "username": user.username},
                status=status.HTTP_201_CREATED
            )            
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
