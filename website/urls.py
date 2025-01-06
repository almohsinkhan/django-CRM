from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('User/<int:pk>', views.User_Record, name='User'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('add_record/', views.add_record, name='add_record'),
    path('edit_record/<int:pk>', views.edit_record, name='edit_record'),
]
