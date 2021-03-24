from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Employee, DirectDeposit, Benefits, directdeposit, benefits, employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Employee"""
    class Meta:
        model = Employee
        url = serializers.HyperlinkedIdentityField(
            view_name='employee', lookup_field='id'
        )
        fields = ('id', 'user', 'benefits_id')
        depth = 1

class Employees(ViewSet):

    def update(self, request, pk=None):
        """
        @api {PUT} /customers/:id PUT changes to employee benefits and deposit accounts
        @apiName UpdateEmployee
        @apiGroup Employee
        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611
        @apiParam {id} id Customer Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        employee = Employee.objects.get(user=request.auth.user)
        benefits = Benefits.objects.get(pk=pk)
        employee.benefits_id = benefits
        employee.user.save()
        employee.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer
        Purpose: Allow a user to communicate with the Arsenal database to retrieve  one user
        Methods:  GET
        Returns:
            Response -- JSON serialized employee or student instance
        """
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        """Handle GET requests to employee resource"""
        employees = Employee.objects.all()

        user = self.request.query_params.get('user', None)

        if user is not None:
            employees = employees.filter(user__pk=user)

        serializer = EmployeeSerializer(
            employees, many=True, context={'request': request})
        return Response(serializer.data)