from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import DirectDeposit, directdeposit, employee
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DirectDepositSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = DirectDeposit
        url = serializers.HyperlinkedIdentityField(
            view_name='directdeposit',
            lookup_field='id'
        )
        fields = ('id', 'account_number', 'routing_number', 'bank_name', 'employee','account_name')


class DirectDeposits(ViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized direct deposit instance
        """
        new_direct_deposit = DirectDeposit()
        new_direct_deposit.account_number = request.data["account_number"]
        new_direct_deposit.routing_number = request.data["routing_number"]
        new_direct_deposit.bank_name = request.data["bank_name"]
        new_direct_deposit.employee = employee
        new_direct_deposit.account_name = request.data["account_name"]
        new_direct_deposit.save()

        serializer = DirectDepositSerializer(new_direct_deposit, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single deposit accounts"""
        try:
            direct_deposit = DirectDeposit.objects.get(pk=pk)
            serializer = DirectDepositSerializer(direct_deposit, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a employee deposit account
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            direct_deposit = DirectDeposit.objects.get(pk=pk)
            direct_deposit.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except DirectDeposit.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to direct deposit resource"""
        direct_deposit = DirectDeposit.objects.all()
        serializer = DirectDepositSerializer(
            direct_deposit, many=True, context={'request': request})
        return Response(serializer.data)