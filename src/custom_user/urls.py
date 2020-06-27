from django.urls import path
from .views import UserListCreateAPIView, UserLogin, PasswordChangeUpdateApiView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-api-view', ),
    path('login/', UserLogin.as_view(), name='user-login-api'),
    path('users/<int:id>/', PasswordChangeUpdateApiView.as_view(), name='password-change')


]
