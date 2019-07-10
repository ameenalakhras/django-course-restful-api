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









# # from snippets.models import Snippet
# from .models import Book
# from book_exchange.models import Book, Contact_info
# from book_exchange.serializers import BookSerializer, ContactInfoSerializer
# from rest_framework import generics, permissions
#
#
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
# # class SingleBook(generics.ListCreateAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
# #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
#
# class ContactList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
#
# #
# # class SnippetList(generics.ListCreateAPIView):
# #     queryset = Contact_info.objects.all()
# #     serializer_class = ContactInfoSerializer
# #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# #
# #     # override the origional saving to make the user required when saving a snippet as an instance of the request as the "owner" field
# #     def perform_create(self, serializer):
# #         serializer.save(owner=self.request.user)
# #
# # class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Snippet.objects.all()
# #     serializer_class = SnippetSerializer
# #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
