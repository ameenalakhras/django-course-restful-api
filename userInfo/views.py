from userInfo.models import ContactInfo, Offer
from rest_framework import viewsets
from rest_framework.response import Response
from restProject.serializers import IsOwnerOrReadOnly#, IsMadeOrReadOnly
from rest_framework.permissions import IsAuthenticated
from userInfo.serializers import ContactInfoSerializer, OfferSerializer
# from django.db.utils import IntegrityError


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]#, IsMadeOrReadOnly]
    def get(self, request):
        serializer = ContactInfoSerializer(self.queryset, many=True)
        return Response(serializer.data)


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request):
        serializer = OfferSerializer(self.queryset, many=True)
        return Response(serializer.data)
