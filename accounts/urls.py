from accounts.views import UserViewSet
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_change/', views.ChangePasswordView.as_view(), name='change-password'),
    path('login/', views.login),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('refresh_token/', views.refresh_token),
    path('test/', views.test),
]
