                    ############################# MY OLD CODE #############################
# from rest_framework import serializers
# # from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight
# from book_exchange.models import Book
#
# BOOK_STATUS_OPTIONS = (
#     ("sale", "sale"),
#     ("giveaway", "giveaway")
# )
#
#
#
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # status = serializers.ChoiceField(choices=BOOK_STATUS_OPTIONS, default='sale')
#     category = serializers.ChoiceField(choices=BOOK_STATUS_OPTIONS, default='sale')
#     # category = models.ForeignKey(Category, related_name = "category", on_delete = models.CASCADE)
#     status =  serializers.ChoiceField(choices=BOOK_STATUS_OPTIONS, default='sale')# (sale, givaway)
#     availability = serializers.BooleanField(default=False)
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     def create(self, validated_data):
#         """
#         create and return a new "book" instance
#         """
#         return Book.objects.create(**validated_data)
#
#
#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'status', 'availability', 'owner')
#
#
# class ContactInfoSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     phone = serializers.CharField(max_length=30)
#     email = serializers.CharField(max_length=60)
                        ############################# THE NEW CODE #############################

from rest_framework import serializers
from book_exchange.models import Book
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
