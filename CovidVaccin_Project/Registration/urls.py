from . import views
from django.urls import path
app_name = 'Registration'

urlpatterns = [
    path('register',views.register,name='Register'),
    path('login',views.Login,name='Login'),
    path('logout',views.logout,name='logout'),
    path('user_details',views.User_Details,name='User_Details'),

    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
]