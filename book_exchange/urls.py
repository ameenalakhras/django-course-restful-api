from rest_framework import routers
from .views import BookViewSet, categoryViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'category', categoryViewSet)


urlpatterns = router.urls












# from django.contrib import admin
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import BookList, BookDetail
# urlpatterns = [
#     path("books/",BookList.as_view() ),
#     path('books/<int:pk>', BookDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = format_suffix_patterns(urlpatterns)
