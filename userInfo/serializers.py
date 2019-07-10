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
