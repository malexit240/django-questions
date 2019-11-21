from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('<int:question_id>/',detail,name='detail'),
    path('<int:question_id>/result',result,name='result'),
    path('<int:question_id>/vote',vote,name='vote'),
    path('',index,name='index'),
]