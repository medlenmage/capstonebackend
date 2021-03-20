from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Benefits

class BenefitsSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = Benefits
        url = serializers.HyperlinkedIdentityField(
            view_name='benefits',
            lookup_field='id'
        )
        fields = ('id', 'health_ins', 'dental_ins', 'life_ins', 'vacation_days', 'sick_days')


class Benefit(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single benefits"""
        try:
            benefit = Benefits.objects.get(pk=pk)
            serializer = BenefitsSerializer(benefit, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to direct deposit resource"""
        benefit = Benefits.objects.all()
        serializer = BenefitsSerializer(
            benefit, many=True, context={'request': request})
        return Response(serializer.data)