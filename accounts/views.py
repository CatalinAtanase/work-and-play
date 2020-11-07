from django.conf import settings
import jwt
from rest_framework.generics import CreateAPIView, UpdateAPIView
from accounts.utils import generate_access_token, set_refresh_token, generate_refresh_token
from django.shortcuts import render
from rest_framework import viewsets, exceptions, status
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer, UserSerializer
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import requires_csrf_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@ensure_csrf_cookie
def login(request):
    User = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'email and password required')

    user = User.objects.filter(email=email).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found') #Change to invalid credentials
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    user.token_version = user.token_version + 1
    user.save()

    access_token, access_token_lifetime = generate_access_token(user)

    response.data = {
        'access_token': access_token,
        'user': serialized_user,
        'access_token_lifetime': access_token_lifetime
    }

    if settings.DEBUG:
        set_refresh_token(user, user.token_version, response)
        refresh_token = generate_refresh_token(user, user.token_version)
        response.data['refresh_token'] = refresh_token
    else:
        set_refresh_token(user, user.token_version, response)

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@ensure_csrf_cookie
@requires_csrf_token
def refresh_token(request):
    '''
    To obtain a new access_token this view expects 2 important things:
        1. a cookie that contains a valid refresh_token
        2. a header 'X-CSRFTOKEN' with a valid csrf token, client app can get it from cookies "csrftoken"
    '''
    User = get_user_model()

    refresh_token = request.COOKIES.get('refresh_token')
    response = Response()

    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided. Cookie missing')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')
    except jwt.DecodeError:
        raise exceptions.AuthenticationFailed(
            'Invalid token.')

    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')

    if payload['token_version'] != user.token_version:
        raise exceptions.AuthenticationFailed('Invalid Token')

    access_token, access_token_lifetime = generate_access_token(user)

    response.data = {
        'access_token': access_token,
        'user': UserSerializer(user).data,
        'access_token_lifetime': access_token_lifetime,
    }

    if settings.DEBUG:
        set_refresh_token(user, user.token_version, response)
        refresh_token = generate_refresh_token(user, user.token_version)
        response.data['refresh_token'] = refresh_token
    else:
        set_refresh_token(user, user.token_version, response)

    return response


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }
        # return new token
        return Response(response, status=status.HTTP_200_OK)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny # Or anon users can't register
    ]
    authentication_classes = []
    serializer_class = UserSerializer


@api_view(['POST'])
@requires_csrf_token
@ensure_csrf_cookie
def test(request):
    response = Response()
    serialized_user = UserSerializer(request.user).data
    response.data = {
        'user': serialized_user
    }

    return response
