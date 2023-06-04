from django.urls import path
from ranking import views

urlpatterns = [
    path('', views.index, name='ranking')
]