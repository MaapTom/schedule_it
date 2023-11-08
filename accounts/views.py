from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from schedule.models import Scheduling
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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
def mgm_erro(request):
                mensagem = "Já existe esse usuário!!"
                script = f'''
                    <script>
                        alert("{mensagem}");
                        window.history.back();  
                    </script>
                '''
                return HttpResponse(script)
            

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
            return mgm_erro(request)

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name)

        if hasattr(user, 'contact'):
            user.contact.phone = phone
            user.contact.save()
        return render(request, 'login.html')

# ----------------------------------------------------------------------------------------------------

@login_required
def home(request):
    if request.user.is_authenticated:
        # Isso obtém todos os registros, ajuste conforme necessário
        schedule_data = Scheduling.objects.all()
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        return render(request, 'home.html', {'schedule_data': user})
    return render(request, 'login.html')


# ---------------------------LOGOUT-------------------------------------------------------------------------

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')