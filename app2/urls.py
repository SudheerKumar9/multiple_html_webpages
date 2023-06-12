from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('cricketpage/',cricketpage,name='cricketpage'),
    path('cssboxmodel/',cssboxmodel,name='cssboxmodel'),
    path('cssbackgrounds/',cssbackgrounds,name='cssbackgrounds'),
    path('webmodal/',webmodal,name='webmodal'),
    path('navbar/',navbar,name='navbar'),
    path('swiggycart/',swiggycart,name='swiggycart'),
    path('javajamcoffee/',javajamcoffee,name='javajamcoffee'),
    path('equiliser/',equiliser,name='equiliser'),
    path('cssrotate/',cssrotate,name='cssrotate'),
]