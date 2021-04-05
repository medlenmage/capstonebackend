from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Student, Employee, Grouping, grouping
from .employee import EmployeeSerializer


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = Student
        url = serializers.HyperlinkedIdentityField(
            view_name='student',
            lookup_field='id'
        )
        fields = ('user')

class GroupingSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = Grouping
        url = serializers.HyperlinkedIdentityField(
            view_name='grouping',
            lookup_field='id'
        )
        fields = ('student', 'employee', 'start_date', 'end_date')


class Groupings(ViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized equipment instance
        """
        new_grouping = Grouping()
        new_grouping.student = request.data["student"]
        new_grouping.employee = request.data["employee"]
        new_grouping.start_date = request.data["start_date"]
        new_grouping.end_date = request.data["end_date"]
        new_grouping.save()

        serializer = GroupingSerializer(new_grouping, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single equipment"""
        try:
            grouping = Grouping.objects.get(pk=pk)
            serializer = GroupingSerializer(grouping, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a employee deposit account
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            grouping = Grouping.objects.get(pk=pk)
            grouping.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Grouping.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to direct deposit resource"""
        grouping = Grouping.objects.all()
        serializer = GroupingSerializer(
            grouping, many=True, context={'request': request})
        return Response(serializer.data)