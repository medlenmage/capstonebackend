from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import DirectDeposit, directdeposit
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DirectDepositSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = DirectDeposit
        url = serializers.HyperlinkedIdentityField(
            view_name='directdeposit',
            lookup_field='id'
        )
        fields = ('id', 'account_number', 'routing_number', 'bank_name', 'account_name')


class DirectDeposit(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized direct deposit instance
        """
        new_direct_deposit = DirectDeposit()
        new_direct_deposit.name = request.data["account_name"]
        new_direct_deposit.save()

        serializer = DirectDepositSerializer(new_direct_deposit, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single deposit accounts"""
        try:
            category = DirectDeposit.objects.get(pk=pk)
            serializer = DirectDepositSerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to DirectDeposit resource"""
        direct_deposit = DirectDeposit.objects.all()

        serializer = DirectDepositSerializer(
            direct_deposit, many=True, context={'request': request})
        return Response(serializer.data)