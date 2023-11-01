from django.shortcuts import render, redirect
from .forms import SchedulingForm
# Importe a classe Scheduling do seu arquivo models.py
from .models import Scheduling
from django.contrib.auth.decorators import login_required


@login_required
def create_scheduling(request):
    if request.method == 'POST':
        form = SchedulingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            # Redirecione para a página desejada após o salvamento bem-sucedido.
            return redirect('home')
    else:
        form = SchedulingForm()

    return render(request, 'schedule.html', {'form': form})
