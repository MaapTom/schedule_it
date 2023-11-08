from django.urls import path
from .views import login, register, home, logout_view


urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('logout', logout_view, name="logout"),
]
