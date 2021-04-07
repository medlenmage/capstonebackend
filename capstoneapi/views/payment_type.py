from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import PaymentType
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = PaymentType
        url = serializers.HyperlinkedIdentityField(
            view_name='paymenttype',
            lookup_field='id'
        )
        fields = ('id', 'account_number', 'routing_number', 'bank_name','payment_name')


class PaymentTypes(ViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized direct deposit instance
        """
        new_payment_type = PaymentType()
        new_payment_type.account_number = request.data["account_number"]
        new_payment_type.routing_number = request.data["routing_number"]
        new_payment_type.bank_name = request.data["bank_name"]
        new_payment_type.account_name = request.data["account_name"]
        new_payment_type.save()

        serializer = PaymentTypeSerializer(new_payment_type, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single deposit accounts"""
        try:
            payment_type = PaymentType.objects.get(pk=pk)
            serializer = PaymentTypeSerializer(payment_type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a employee deposit account
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            payment_type = PaymentType.objects.get(pk=pk)
            payment_type.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to direct deposit resource"""
        payment_type = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(
            payment_type, many=True, context={'request': request})
        return Response(serializer.data)