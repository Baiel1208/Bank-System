from rest_framework.routers import DefaultRouter

from users.views import UserAPIView

router = DefaultRouter()
router.register('user', UserAPIView, 'api_users')

urlpatterns = router.urls