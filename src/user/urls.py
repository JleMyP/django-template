from django.urls import path
from rest_framework_simplejwt.views import token_refresh, token_verify

from .views import CustomTokenObtainView, ProfileView, RegistrationView

urlpatterns = [
    path('api/v1/registration/', RegistrationView.as_view(), name='registration'),
    path('api/v1/token/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', token_refresh, name='token_refresh'),
    path('api/v1/token/verify/', token_verify, name='token_verify'),
    path('api/v1/profile/', ProfileView.as_view(), name='profile'),
]
