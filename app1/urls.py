from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('formreg/',formreg,name='formreg'),
    path('jspiders/',jspiders,name='jspiders'),
    path('semantictags/',semantictags,name='semantictags'),
    path('resumetask/',resumetask,name='resumetask'),
    path('onlinejobform/',onlinejobform,name='onlinejobform'),
    path('menubar/',menubar,name='menubar'),

    
]