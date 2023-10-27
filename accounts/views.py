from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('Usuario ou Senha invalido')

# -------------------------------------------------------------------------


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        first_name = request.POST.get('full_name')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe esse usuario!!')

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name)

        if hasattr(user, 'contact'):
            user.contact.phone = phone
            user.contact.save()

        # return HttpResponse('Usuario Cadastrado com sucesso !!')

        return render(request, 'login.html')

# ----------------------------------------------------------------------------------------------------


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request, 'login.html')
