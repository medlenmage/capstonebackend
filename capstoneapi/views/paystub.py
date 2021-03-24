from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Paystub, paystub


class PaystubSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee paystubs"""
    class Meta:
        model = Paystub
        url = serializers.HyperlinkedIdentityField(
            view_name='paystub',
            lookup_field='id'
        )
        fields = ('id', 'employee_id', 'salary', 'pay_period', 'deposit_date', 'deposit_account')
        depth = 2


class Paystubs(ViewSet):

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized direct deposit instance
        """
        new_paystub = Paystub()
        new_paystub.employee_id = request.data["employee_id"]
        new_paystub.salary = request.data["salary"]
        new_paystub.pay_period = request.data["pay_period"]
        new_paystub.deposit_date = request.data["deposit_date"]
        new_paystub.deposit_account = request.data["deposit_account"]
        new_paystub.save()

        serializer = PaystubSerializer(new_paystub, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single paystub"""
        try:
            paystub = Paystub.objects.get(pk=pk)
            serializer = PaystubSerializer(paystub, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        """Handle GET requests to paystub resource"""
        paystub = Paystub.objects.all()

        employee_id = self.request.query_params.get('employee_id', None)

        if employee_id is not None:
            paystub = paystub.filter(employee_id__pk=employee_id)

        serializer = PaystubSerializer(
            paystub, many=True, context={'request': request})
        return Response(serializer.data)