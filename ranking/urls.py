from django.urls import path
from ranking import views

urlpatterns = [
    path('', views.index, name='ranking'),
    path('economic_blast_wave', views.economic_blast_wave, name='economic-blast-wave'),
    path('update_economic_blast_wave', views.update_economic_blast_wave, name='update-economic_blast_wave'),

]