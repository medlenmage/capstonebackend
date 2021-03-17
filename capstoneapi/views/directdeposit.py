from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import DirectDeposit
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = DirectDeposit
        url = serializers.HyperlinkedIdentityField(
            view_name='directdeposit',
            lookup_field='id'
        )
        fields = ('id', 'account_number', 'routing_number', 'bank_name', 'account_name')