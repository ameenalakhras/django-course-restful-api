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



from book_exchange.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.response import Response
from restProject.serializers import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request):
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)
