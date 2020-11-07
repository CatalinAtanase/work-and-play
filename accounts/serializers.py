from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
from rest_framework import serializers
from rest_framework.decorators import api_view
from accounts.models import User, UserProfile
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _


class UserProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "image",
        )


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    user_profile = UserProfileSerialzer()

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'user_profile',
            'team',
            'is_staff',
            'first_name',
            'last_name',
            'is_active',
            'created_at',
            'updated_at',
            'token_version',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(
        max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(
        max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError(
                {'new_password2': _("The two password fields didn't match.")})
        password_validation.validate_password(
            data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user



