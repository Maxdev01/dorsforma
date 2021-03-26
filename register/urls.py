
from django.urls import path 
from .views import views_form

urlpatterns = [
    path('', views_form , name='vu'),
]



