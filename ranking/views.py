from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from .forms import *


def check_if_request_user_answered_ranking(request_user, ranking):
    return ranking.filter(author_id=request_user).exists()


# Create your views here.
@login_required(login_url='register')
@never_cache
def index(request):
    if not request.user.is_authenticated:
        return redirect('register')
    else:
        user = request.user.id

        economic_blast_fireball_status = check_if_request_user_answered_ranking(user,
                                                                                EconomicBlastFireBall.objects.all().values())
        social_blast_fireball_status = check_if_request_user_answered_ranking(user,
                                                                              SocialBlastFireBall.objects.all().values())
        environmental_blast_fireball_status = check_if_request_user_answered_ranking(user,
                                                                                     EnvironmentalBlastFireBall.objects.all().values())

        any_column_is_ready = True if any(
            [all([economic_blast_fireball_status]),
             all([social_blast_fireball_status]),
             all([environmental_blast_fireball_status])]) else False

        context = {
            'economic_status': economic_blast_fireball_status,
            'social_status': social_blast_fireball_status,
            'environmental_status': environmental_blast_fireball_status,
            'any_column_is_ready': any_column_is_ready
        }
        return render(request, 'ranking/criteria_table_shorten.html', context)


# Economical
def economic_blast_wave(request):
    if request.method == 'POST':
        form = EconomicBlastShockWaveForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EconomicBlastShockWave.objects.all().values())
        if is_answered:
            return redirect('update-economic-blast-wave')
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


def economic_fire(request):
    if request.method == 'POST':
        form = EconomicFireForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EconomicFire.objects.all().values())
        if is_answered:
            return redirect('update-economic-fire')
        else:
            form = EconomicFireForm()
    return render(request, 'ranking/economic_fire.html', {'form': form})


def update_economic_fire(request):
    ranking = EconomicFire.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = EconomicFireForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EconomicFireForm(instance=ranking)
    return render(request, 'ranking/economic_fire.html', {'form': form})


def economic_blast_fireball(request):
    if request.method == 'POST':
        form = EconomicBlastFireBallForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EconomicBlastFireBall.objects.all().values())
        if is_answered:
            return redirect('update-economic-blast-fireball')
        else:
            form = EconomicBlastFireBallForm()
    return render(request, 'ranking/economic_blast_fire_ball.html', {'form': form})


def update_economic_blast_fireball(request):
    ranking = EconomicBlastFireBall.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = EconomicBlastFireBallForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EconomicBlastFireBallForm(instance=ranking)
    return render(request, 'ranking/economic_blast_fire_ball.html', {'form': form})


# Social

def social_blast_wave(request):
    if request.method == 'POST':
        form = SocialBlastShockWaveForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             SocialBlastShockWave.objects.all().values())
        if is_answered:
            return redirect('update-social-blast-wave')
        else:
            form = SocialBlastShockWaveForm()
    return render(request, 'ranking/social_blast_shock_wave.html', {'form': form})


def update_social_blast_wave(request):
    ranking = SocialBlastShockWave.objects.filter(author=request.user).first()
    if request.method == 'POST':
        form = SocialBlastShockWaveForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = SocialBlastShockWaveForm(instance=ranking)
    return render(request, 'ranking/social_blast_shock_wave.html', {'form': form})


def social_fire(request):
    if request.method == 'POST':
        form = SocialFireForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             SocialFire.objects.all().values())
        if is_answered:
            return redirect('update-social-fire')
        else:
            form = SocialFireForm()
    return render(request, 'ranking/social_fire.html', {'form': form})


def update_social_fire(request):
    ranking = SocialFire.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = SocialFireForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = SocialFireForm(instance=ranking)
    return render(request, 'ranking/social_fire.html', {'form': form})


def social_blast_fireball(request):
    if request.method == 'POST':
        form = SocialBlastFireBallForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             SocialBlastFireBall.objects.all().values())
        if is_answered:
            return redirect('update-social-blast-fireball')
        else:
            form = SocialBlastFireBallForm()
    return render(request, 'ranking/social_blast_fire_ball.html', {'form': form})


def update_social_blast_fireball(request):
    ranking = SocialBlastFireBall.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = SocialBlastFireBallForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = SocialBlastFireBallForm(instance=ranking)
    return render(request, 'ranking/social_blast_fire_ball.html', {'form': form})


# Environmental

def environmental_blast_wave(request):
    if request.method == 'POST':
        form = EnvironmentalBlastShockWaveForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EnvironmentalBlastShockWave.objects.all().values())
        if is_answered:
            return redirect('update-environmental-blast-wave')
        else:
            form = EnvironmentalBlastShockWaveForm()
    return render(request, 'ranking/environmental_blast_shock_wave.html', {'form': form})


def update_environmental_blast_wave(request):
    ranking = EnvironmentalBlastShockWave.objects.filter(author=request.user).first()
    if request.method == 'POST':
        form = EnvironmentalBlastShockWaveForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EnvironmentalBlastShockWaveForm(instance=ranking)
    return render(request, 'ranking/environmental_blast_shock_wave.html', {'form': form})


def environmental_fire(request):
    if request.method == 'POST':
        form = EnvironmentalFireForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EnvironmentalFire.objects.all().values())
        if is_answered:
            return redirect('update-environmental-fire')
        else:
            form = EnvironmentalFireForm()
    return render(request, 'ranking/environmental_fire.html', {'form': form})


def update_environmental_fire(request):
    ranking = EnvironmentalFire.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = EnvironmentalFireForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EnvironmentalFireForm(instance=ranking)
    return render(request, 'ranking/environmental_fire.html', {'form': form})


def environmental_blast_fireball(request):
    if request.method == 'POST':
        form = EnvironmentalBlastFireBallForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EnvironmentalBlastFireBall.objects.all().values())
        if is_answered:
            return redirect('update-environmental-blast-fireball')
        else:
            form = EnvironmentalBlastFireBallForm()
    return render(request, 'ranking/environmental_blast_fire_ball.html', {'form': form})


def update_environmental_blast_fireball(request):
    ranking = EnvironmentalBlastFireBall.objects.all().filter(author=request.user).first()
    if request.method == 'POST':
        form = EnvironmentalBlastFireBallForm(request.POST, instance=ranking)
        if form.is_valid():
            form.save()
            return redirect('ranking')

    else:
        form = EnvironmentalBlastFireBallForm(instance=ranking)
    return render(request, 'ranking/environmental_blast_fire_ball.html', {'form': form})


def economic_ranking(request):
    if request.method == 'POST':
        form_blast_wave = EconomicBlastShockWaveForm(request.POST)
        form_fire = EconomicFireForm(request.POST)
        form_fire_ball = EconomicBlastFireBallForm(request.POST)

        form_blast_wave.instance.author = request.user
        form_fire.instance.author = request.user
        form_fire_ball.instance.author = request.user
        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EconomicBlastShockWave.objects.all().values())
        if is_answered:
            return redirect('update-economic-ranking')
        else:
            form_blast_wave = EconomicBlastShockWaveForm()
            form_fire = EconomicFireForm()
            form_fire_ball = EconomicBlastFireBallForm()
    return render(request, 'ranking/economic_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})


def update_economic_ranking(request):
    blast_wave_ranking = EconomicBlastShockWave.objects.filter(author=request.user).first()
    fire_ranking = EconomicFire.objects.filter(author=request.user).first()
    blast_fire_ball_ranking = EconomicBlastFireBall.objects.filter(author=request.user).first()

    if request.method == 'POST':
        form_blast_wave = EconomicBlastShockWaveForm(request.POST, instance=blast_wave_ranking)
        form_fire = EconomicFireForm(request.POST, instance=fire_ranking)
        form_fire_ball = EconomicBlastFireBallForm(request.POST, instance=blast_fire_ball_ranking)

        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        form_blast_wave = EconomicBlastShockWaveForm(instance=blast_wave_ranking)
        form_fire = EconomicFireForm(instance=fire_ranking)
        form_fire_ball = EconomicBlastFireBallForm(instance=blast_fire_ball_ranking)
    return render(request, 'ranking/economic_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})


def social_ranking(request):
    if request.method == 'POST':
        form_blast_wave = SocialBlastShockWaveForm(request.POST)
        form_fire = SocialFireForm(request.POST)
        form_fire_ball = SocialBlastFireBallForm(request.POST)

        form_blast_wave.instance.author = request.user
        form_fire.instance.author = request.user
        form_fire_ball.instance.author = request.user
        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             SocialBlastFireBall.objects.all().values())
        if is_answered:
            return redirect('update-social-ranking')
        else:
            form_blast_wave = SocialBlastShockWaveForm()
            form_fire = SocialFireForm()
            form_fire_ball = SocialBlastFireBallForm()
    return render(request, 'ranking/social_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})


def update_social_ranking(request):
    blast_wave_ranking = SocialBlastShockWave.objects.all().filter(author=request.user).first()
    fire_ranking = SocialFire.objects.all().filter(author=request.user).first()
    blast_fire_ball_ranking = SocialBlastFireBall.objects.all().filter(author=request.user).first()

    if request.method == 'POST':
        form_blast_wave = SocialBlastShockWaveForm(request.POST, instance=blast_wave_ranking)
        form_fire = SocialFireForm(request.POST, instance=fire_ranking)
        form_fire_ball = SocialBlastFireBallForm(request.POST, instance=blast_fire_ball_ranking)

        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        form_blast_wave = SocialBlastShockWaveForm(instance=blast_wave_ranking)
        form_fire = SocialFireForm(instance=fire_ranking)
        form_fire_ball = SocialBlastFireBallForm(instance=blast_fire_ball_ranking)
    return render(request, 'ranking/social_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})


def environmental_ranking(request):
    if request.method == 'POST':
        form_blast_wave = EnvironmentalBlastShockWaveForm(request.POST)
        form_fire = EnvironmentalFireForm(request.POST)
        form_fire_ball = EnvironmentalBlastFireBallForm(request.POST)

        form_blast_wave.instance.author = request.user
        form_fire.instance.author = request.user
        form_fire_ball.instance.author = request.user

        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        is_answered = check_if_request_user_answered_ranking(request.user.id,
                                                             EnvironmentalBlastFireBall.objects.all().values())
        if is_answered:
            return redirect('update-environmental-ranking')
        else:
            form_blast_wave = EnvironmentalBlastShockWaveForm()
            form_fire = EnvironmentalFireForm()
            form_fire_ball = EnvironmentalBlastFireBallForm()
    return render(request, 'ranking/environmental_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})


def update_environmental_ranking(request):

    blast_wave_ranking = EnvironmentalBlastShockWave.objects.all().filter(author=request.user).first()
    fire_ranking = EnvironmentalFire.objects.all().filter(author=request.user).first()
    blast_fire_ball_ranking = EnvironmentalBlastFireBall.objects.all().filter(author=request.user).first()

    if request.method == 'POST':
        form_blast_wave = EnvironmentalBlastShockWaveForm(request.POST, instance=blast_wave_ranking)
        form_fire = EnvironmentalFireForm(request.POST, instance=fire_ranking)
        form_fire_ball = EnvironmentalBlastFireBallForm(request.POST, instance=blast_fire_ball_ranking)

        if form_blast_wave.is_valid() and form_fire.is_valid() and form_fire_ball.is_valid():
            form_blast_wave.save()
            form_fire.save()
            form_fire_ball.save()
            return redirect('ranking')

    else:
        form_blast_wave = EnvironmentalBlastShockWaveForm(instance=blast_wave_ranking)
        form_fire = EnvironmentalFireForm(instance=fire_ranking)
        form_fire_ball = EnvironmentalBlastFireBallForm(instance=blast_fire_ball_ranking)
    return render(request, 'ranking/environmental_ranking.html',
                  {'form_blast_wave': form_blast_wave, 'form_fire': form_fire, 'form_fire_ball': form_fire_ball})
