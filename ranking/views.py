from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .utils import check_if_request_user_answered_ranking


# Create your views here.

@login_required(login_url='register')
def index(request):
    status = check_if_request_user_answered_ranking(request.user.id,
                                                    EconomicBlastShockWave.objects.all().values())

    return render(request, 'ranking/ranking_view.html', {'status': status})


def economic_blast_wave(request):
    if request.method == 'POST':
        form = EconomicBlastShockWaveForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        # Проверить, заполнял ли пользователь уже форму - направить на апдейт
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EconomicBlastShockWave.objects.all().values())
        if is_answered:
            return redirect('update-economic_blast_wave')
        else:
            form = EconomicBlastShockWaveForm()
    return render(request, 'ranking/economic_blast_shock_wave.html', {'form': form})


def update_economic_blast_wave(request):
    ranking = EconomicBlastShockWave.objects.filter(author=request.user).first()
    if request.method == 'POST':
        form = EconomicBlastShockWaveForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EconomicBlastShockWaveForm(instance=ranking)
    return render(request, 'ranking/economic_blast_shock_wave.html', {'form': form})
