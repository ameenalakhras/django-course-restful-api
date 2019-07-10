from book_exchange.models import Book, Category
from rest_framework import viewsets
from .serializers import BookSerializer, CategorySerializer
from rest_framework.response import Response
from restProject.serializers import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    def get(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)

class categoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
