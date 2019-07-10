from rest_framework import serializers
# from rest_framework.decorators import api_view, permission_classes
from restProject.serializers import IsOwnerOrReadOnly
from userInfo.models import ContactInfo, Offer


class ContactInfoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = ContactInfo
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Offer
        fields = '__all__'


#
# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('category', 'in_stock')
#
#
# @permission_classes((IsOwnerOrReadOnly,))
# class BookSerializer(serializers.ModelSerializer):
#     owner = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     class Meta:
#         model = Book
#         fields = ('title','category','status','availability','owner')
