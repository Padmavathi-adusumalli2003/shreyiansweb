from django.urls import path
from .views import *
app_name='myapp'
urlpatterns=[
    path('',home,name='home'),
    path('course/',course,name='course'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('request/',request,name='request'),
    path('sign/',sign,name='sign'),
    path('email/',email,name='email')
]