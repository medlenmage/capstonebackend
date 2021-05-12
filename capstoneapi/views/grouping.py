from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Student, Employee, Grouping, grouping
from .employee import EmployeeSerializer
from .student import StudentSerializer

class GroupingSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = Grouping
        url = serializers.HyperlinkedIdentityField(
            view_name='groupings',
            lookup_field='id'
        )
        fields = ('id', 'student', 'instructor', 'start_date', 'end_date')
        depth = 3



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

        instructor = self.request.query_params.get('instructor', None)

        if instructor is not None:
            grouping = grouping.filter(instructor__pk=instructor)
            
        serializer = GroupingSerializer(
            grouping, many=True, context={'request': request})
        return Response(serializer.data)