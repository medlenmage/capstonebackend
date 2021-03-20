from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Equipment, equipment


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = Equipment
        url = serializers.HyperlinkedIdentityField(
            view_name='equipment',
            lookup_field='id'
        )
        fields = ('id', 'equipment_type', 'is_available')


class Equipment(ViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized equipment instance
        """
        new_equipment = Equipment()
        new_equipment.equipment_type = request.data["equipment_type"]
        new_equipment.is_available = request.data["is_available"]
        new_equipment.save()

        serializer = EquipmentSerializer(new_equipment, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        @api {PUT} /customers/:id PUT changes to equipment
        @apiName UpdateEquipment
        @apiGroup Equipment
        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611
        @apiParam {id} id Equipment Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        equipment = Equipment.objects.get()
        equipment.equipment_type = request.data["equipment_type"]
        equipment.is_available = request.data["is_available"]
        equipment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single equipment"""
        try:
            equipment = Equipment.objects.get(pk=pk)
            serializer = EquipmentSerializer(equipment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a employee deposit account
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            equipment = Equipment.objects.get(pk=pk)
            equipment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Equipment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to direct deposit resource"""
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(
            equipment, many=True, context={'request': request})
        return Response(serializer.data)