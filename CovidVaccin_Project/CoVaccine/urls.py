from . import views
from django.urls import path
app_name = 'CoVaccine'

urlpatterns = [
    path('',views.Home,name='Home'),
]