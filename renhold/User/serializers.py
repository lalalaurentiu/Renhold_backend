from rest_framework import serializers
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.

    This serializer is used to convert CustomUser model instances to JSON
    representation and vice versa. It provides validation for the email field
    and handles the creation and saving of CustomUser instances.

    Attributes:
        email: A required EmailField for the user's email address.
    """

    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email']
        read_only_fields = ['id', 'date_joined']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['email'] = _(representation['email'])
        return representation
    
    def save(self, **kwargs):
        user = CustomUser.objects.filter(email=self.validated_data['email'])
        if user.exists():
            return user.first()
        return super().save(**kwargs)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
