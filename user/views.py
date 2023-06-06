from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from user.forms import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email[:user.email.index("@")]
            user.save()
            login(request, user)
            return redirect('ranking')
        else:
            if form.has_error('email'):
                return render(request, 'user/already_done_view.html')

    else:
        form = UserRegisterForm()
    return render(request, 'user/registration_view.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('register')
