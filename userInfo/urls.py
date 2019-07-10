from rest_framework import routers
from userInfo.views import ContactInfoViewSet, OfferViewSet

router = routers.DefaultRouter()

router.register(r'contact', ContactInfoViewSet)
router.register(r'offer', OfferViewSet)

urlpatterns = router.urls
