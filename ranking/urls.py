from django.urls import path
from ranking import views

urlpatterns = [
    path('', views.index, name='ranking'),

    # Economical
    path('economic_blast_wave', views.economic_blast_wave, name='economic-blast-wave'),
    path('update_economic_blast_wave', views.update_economic_blast_wave, name='update-economic-blast-wave'),

    path('economic_fire', views.economic_fire, name='economic-fire'),
    path('update_economic_fire', views.update_economic_fire, name='update-economic-fire'),

    path('economic_blast_fireball', views.economic_blast_fireball, name='economic-blast-fireball'),
    path('update_economic_blast_fireball', views.update_economic_blast_fireball, name='update-economic-blast-fireball'),

    # Social
    path('social_blast_wave', views.social_blast_wave, name='social-blast-wave'),
    path('update_social_blast_wave', views.update_social_blast_wave, name='update-social-blast-wave'),

    path('social_fire', views.social_fire, name='social-fire'),
    path('update_social_fire', views.update_social_fire, name='update-social-fire'),

    path('social_blast_fireball', views.social_blast_fireball, name='social-blast-fireball'),
    path('update_social_blast_fireball', views.update_social_blast_fireball, name='update-social-blast-fireball'),

    # Environmental
    path('environmental_blast_wave', views.environmental_blast_wave, name='environmental-blast-wave'),
    path('update_environmental_blast_wave', views.update_environmental_blast_wave, name='update-environmental-blast-wave'),

    path('environmental_fire', views.environmental_fire, name='environmental-fire'),
    path('update_environmental_fire', views.update_environmental_fire, name='update-environmental-fire'),

    path('environmental_blast_fireball', views.environmental_blast_fireball, name='environmental-blast-fireball'),
    path('update_environmental_blast_fireball', views.update_environmental_blast_fireball, name='update-environmental-blast-fireball'),

]