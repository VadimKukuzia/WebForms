
from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.register, name='register'),
    path('update', views.update, name='update-user'),
    path('log-out', views.log_out, name='log-out'),

]
