from rest_framework import routers
from .views import BookViewSet, categoryViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'category', categoryViewSet)


urlpatterns = router.urls
