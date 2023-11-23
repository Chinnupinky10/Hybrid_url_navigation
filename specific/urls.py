from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('anu/',anu,name='anu'),
    path('puji/',puji,name='puji'), 
]