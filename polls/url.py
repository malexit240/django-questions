from django.contrib import admin
from django.urls import path,include
from django.views.generic import View, TemplateView , RedirectView

from .views import *

app_name = 'polls'

urlpatterns = [
    
    path('<int:question_id>/',DetailsView.as_view(),name='detail'),
    path('<int:question_id>/result',result,name='result'),
    path('<int:question_id>/vote',vote,name='vote'),
    path('',index,name='index'),
    path('',TemplateView.as_view(template_name='polls/index.html')), # for static page
    path('',IndexView.as_view()),
    path('',DetailsView.as_view()),

]