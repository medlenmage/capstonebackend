from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import CompanyContact, companycontact


class CompanyContactSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for employee direct deposits"""
    class Meta:
        model = CompanyContact
        url = serializers.HyperlinkedIdentityField(
            view_name='CompanyContact',
            lookup_field='id'
        )
        fields = ('id', 'company_name', 'contact_name', 'contact_phone_number', 'contact_email')


class CompanyContacts(ViewSet):

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized company contact instance
        """
        new_company_contact = CompanyContact()
        new_company_contact.company_name = request.data["company_name"]
        new_company_contact.contact_name = request.data["contact_name"]
        new_company_contact.contact_phone_number = request.data["contact_phone_number"]
        new_company_contact.contact_email = request.data["contact_email"]
        new_company_contact.save()

        serializer = CompanyContactSerializer(new_company_contact, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        @api {PUT} /customers/:id PUT changes to company contacts
        @apiName UpdateCompanyContact
        @apiGroup CompanyContact
        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611
        @apiParam {id} id Company Contact Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        company_contact = CompanyContact.objects.get(pk=pk)
        company_contact.company_name = request.data["company_name"]
        company_contact.contact_name = request.data["contact_name"]
        company_contact.contact_phone_number = request.data["contact_phone_number"]
        company_contact.contact_email = request.data["contact_email"]
        company_contact.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single deposit accounts"""
        try:
            company_contact = CompanyContact.objects.get(pk=pk)
            serializer = CompanyContactSerializer(company_contact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a company contact
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            companycontact = CompanyContact.objects.get(pk=pk)
            companycontact.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CompanyContact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        """Handle GET requests to company contact resource"""
        equipment = CompanyContact.objects.all()
        serializer = CompanyContactSerializer(
            equipment, many=True, context={'request': request})
        return Response(serializer.data)