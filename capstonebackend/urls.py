from capstoneapi.views.users import Users
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from capstoneapi.models import *
from capstoneapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', Users, 'user')
router.register(r'employees', Employees, 'employee')
router.register(r'directdeposits', DirectDeposits, 'directdeposits')
router.register(r'benefits', Benefit, 'benefits')
router.register(r'paystubs', Paystubs, 'paystubs')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^registerstudent$', register_student),
    url(r'^registeremployee$', register_employee),
    url(r'^login$', login_user),
    url(r'^api-token-auth$', obtain_auth_token),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
]