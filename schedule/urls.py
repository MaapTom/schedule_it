from django.urls import path
from .views import create_scheduling

urlpatterns = [
    path('create-scheduling/', create_scheduling, name='create_scheduling'),
]
