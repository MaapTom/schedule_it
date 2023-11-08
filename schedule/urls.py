from django.urls import path
from .views import create_scheduling, logout_view

urlpatterns = [
    path('create-scheduling/', create_scheduling, name='create_scheduling'),
    path('logout', logout_view, name="logout"),
]
