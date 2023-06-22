from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView

from user.forms import UserRegisterForm


# Create your views here.

def start_page(request):
    return render(request, 'user/info_page.html')


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('update-user')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email[:user.email.index("@")] + user.password[-10:]
            user.save()
            login(request, user)
            return redirect('ranking')
        else:
            if form.has_error('email') or form.has_error('username'):
                return render(request, 'user/already_done_view.html')

    else:
        form = UserRegisterForm()
    return render(request, 'user/index.html', {'form': form})


@login_required(login_url='start-page')
@never_cache
def update(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ranking')
        else:
            if form.has_error('email'):
                return render(request, 'user/already_done_view.html')

    else:
        form = UserRegisterForm(instance=request.user)
    return render(request, 'user/index.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'user/thanks.html')
