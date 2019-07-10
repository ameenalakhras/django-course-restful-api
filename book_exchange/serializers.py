from rest_framework import serializers
from book_exchange.models import Book, Category
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from restProject.serializers import IsOwnerOrReadOnly

# @permission_classes((IsOwnerOrReadOnly,))
class BookSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Book
        fields = ('title','category','status','availability','owner')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
