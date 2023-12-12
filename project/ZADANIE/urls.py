from django.urls import path
from .views import *

urlpatterns = [
    path('myvhod', index, name='myvhod'),
    path('myregistr', vhod, name='myregistr'),
]