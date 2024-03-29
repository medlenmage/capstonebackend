"""Register user"""
import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from capstoneapi.models import Employee, Student, Benefits, DirectDeposit


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user
    Method arguments:
      request -- The full HTTP request object
    '''

    body = request.body.decode('utf-8')
    req_body = json.loads(body)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        name = req_body['username']
        pass_word = req_body['password']
        authenticated_user = authenticate(username=name, password=pass_word)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key, "id": authenticated_user.id})
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

    return HttpResponseNotAllowed(permitted_methods=['POST'])


@csrf_exempt
def register_student(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
    )

    student = Student.objects.create(
        user=new_user
    )

    # Commit the user to the database by saving it
    student.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key, "id": new_user.id})
    return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)

@csrf_exempt
def register_employee(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
    request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        is_staff=True
    )

    employee = Employee.objects.create(
        # benefits_id=Benefits.objects.get(health_ins = 'BCBS of TN', dental_ins = 'BCBS of TN', life_ins = 'Prudential', vacation_days = 14, sick_days = 7),
        # deposit_account=DirectDeposit.objects.get(account_number = 123456, routing_number = 654321, bank_name = 'Regions', account_name = "Josh\'s Bank"),
        user=new_user
    )

    # Commit the user to the database by saving it
    employee.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key, "id": new_user.id})
    return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)

@csrf_exempt
def get_current_user(request):

    req_body = json.loads(request.body.decode())

    try:
        user_id = Token.objects.get(key=req_body['token']).user_id
        data = json.dumps({"user_id": user_id})
        return HttpResponse(data, content_type="application/json")
    except Token.DoesNotExist:
        data = json.dumps(
            {"valid": False, "msg": "No currently authenticated user."})
        return HttpResponse(data, content_type='application/json')