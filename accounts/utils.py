import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    access_token_lifetime = 5
    if settings.DEBUG:
        access_token_lifetime = 5
    

    access_token_payload = {
        'user_id': user.id,
        'token_version': user.token_version,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=access_token_lifetime),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.ACCESS_TOKEN_SECRET, algorithm='HS256').decode('utf-8')
    return access_token, access_token_lifetime


def generate_refresh_token(user, token_version):
    refresh_token_payload = {
        'user_id': user.id,
        'token_version': token_version,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256').decode('utf-8')

    return refresh_token


def set_refresh_token(user, token_version, response):
    response.set_cookie(
        key='refreshtoken',
        value=generate_refresh_token(user, token_version),
        httponly=True,
        max_age=604800,
        samesite='None',
        secure=True,
        # path="/api/auth/refresh_token/"
    )
