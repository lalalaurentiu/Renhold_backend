from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView


@permission_classes([AllowAny])
class LoginOrRegister(APIView):
    """
    API view for user login or registration.

    This view allows users to either log in or register a new account.
    Upon successful login or registration, it returns a response containing
    a refresh token and an access token.

    Methods:
    - post: Handles the POST request for user login or registration.

    Attributes:
    - serializer_class: The serializer class used for validating and saving user data.
    """

    serializer_class = CustomUserSerializer

    def post(self, request):
        """
        Handles the POST request for user login or registration.

        Parameters:
        - request: The HTTP request object containing user data.

        Returns:
        - response: The HTTP response object containing the refresh token and access token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        response = {
            "refresh": str(refresh),
            "access": str(access),
        }

        return Response(response)


class Token(TokenObtainPairView):
    """
    View class for obtaining authentication tokens.
    """

    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to obtain authentication tokens.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object.

        Raises:
            Exception: If an error occurs during token generation.

        """
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response({
                "error": str(e)
            })

        return super().post(request, *args, **kwargs)
