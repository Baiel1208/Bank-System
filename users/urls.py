from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import UserAPIView, UserRegisterAPIView

router = DefaultRouter()
router.register('user', UserAPIView, 'api_users')

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view({'post': 'create'}), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]


urlpatterns += router.urls