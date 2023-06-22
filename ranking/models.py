from django.db import models

from user.models import User


# Create your models here.

# Economic
class EconomicBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    E_blast_wave1 = models.IntegerField(null=False)
    E_blast_wave2 = models.IntegerField(null=False)
    E_blast_wave3 = models.IntegerField(null=False)
    E_blast_wave4 = models.IntegerField(null=False)
    E_blast_wave5 = models.IntegerField(null=False)
    E_blast_wave6 = models.IntegerField(null=False)
    E_blast_wave7 = models.IntegerField(null=False)
    E_blast_wave8 = models.IntegerField(null=False)
    E_blast_wave9 = models.IntegerField(null=False)
    E_blast_wave10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EconomicFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E_fire1 = models.IntegerField(null=False)
    E_fire2 = models.IntegerField(null=False)
    E_fire3 = models.IntegerField(null=False)
    E_fire4 = models.IntegerField(null=False)
    E_fire5 = models.IntegerField(null=False)
    E_fire6 = models.IntegerField(null=False)
    E_fire7 = models.IntegerField(null=False)
    E_fire8 = models.IntegerField(null=False)
    E_fire9 = models.IntegerField(null=False)
    E_fire10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EconomicBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E_fire_ball1 = models.IntegerField(null=False)
    E_fire_ball2 = models.IntegerField(null=False)
    E_fire_ball3 = models.IntegerField(null=False)
    E_fire_ball4 = models.IntegerField(null=False)
    E_fire_ball5 = models.IntegerField(null=False)
    E_fire_ball6 = models.IntegerField(null=False)
    E_fire_ball7 = models.IntegerField(null=False)
    E_fire_ball8 = models.IntegerField(null=False)
    E_fire_ball9 = models.IntegerField(null=False)
    E_fire_ball10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


# Social
class SocialBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S_blast_wave1 = models.IntegerField(null=False)
    S_blast_wave2 = models.IntegerField(null=False)
    S_blast_wave3 = models.IntegerField(null=False)
    S_blast_wave4 = models.IntegerField(null=False)
    S_blast_wave5 = models.IntegerField(null=False)
    S_blast_wave6 = models.IntegerField(null=False)
    S_blast_wave7 = models.IntegerField(null=False)
    S_blast_wave8 = models.IntegerField(null=False)
    S_blast_wave9 = models.IntegerField(null=False)
    S_blast_wave10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class SocialFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S_fire1 = models.IntegerField(null=False)
    S_fire2 = models.IntegerField(null=False)
    S_fire3 = models.IntegerField(null=False)
    S_fire4 = models.IntegerField(null=False)
    S_fire5 = models.IntegerField(null=False)
    S_fire6 = models.IntegerField(null=False)
    S_fire7 = models.IntegerField(null=False)
    S_fire8 = models.IntegerField(null=False)
    S_fire9 = models.IntegerField(null=False)
    S_fire10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class SocialBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S_fire_ball1 = models.IntegerField(null=False)
    S_fire_ball2 = models.IntegerField(null=False)
    S_fire_ball3 = models.IntegerField(null=False)
    S_fire_ball4 = models.IntegerField(null=False)
    S_fire_ball5 = models.IntegerField(null=False)
    S_fire_ball6 = models.IntegerField(null=False)
    S_fire_ball7 = models.IntegerField(null=False)
    S_fire_ball8 = models.IntegerField(null=False)
    S_fire_ball9 = models.IntegerField(null=False)
    S_fire_ball10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


# Environmental
class EnvironmentalBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Env_blast_wave1 = models.IntegerField(null=False)
    Env_blast_wave2 = models.IntegerField(null=False)
    Env_blast_wave3 = models.IntegerField(null=False)
    Env_blast_wave4 = models.IntegerField(null=False)
    Env_blast_wave5 = models.IntegerField(null=False)
    Env_blast_wave6 = models.IntegerField(null=False)
    Env_blast_wave7 = models.IntegerField(null=False)
    Env_blast_wave8 = models.IntegerField(null=False)
    Env_blast_wave9 = models.IntegerField(null=False)
    Env_blast_wave10 = models.IntegerField(null=False)
    Env_blast_wave11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EnvironmentalFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Env_fire1 = models.IntegerField(null=False)
    Env_fire2 = models.IntegerField(null=False)
    Env_fire3 = models.IntegerField(null=False)
    Env_fire4 = models.IntegerField(null=False)
    Env_fire5 = models.IntegerField(null=False)
    Env_fire6 = models.IntegerField(null=False)
    Env_fire7 = models.IntegerField(null=False)
    Env_fire8 = models.IntegerField(null=False)
    Env_fire9 = models.IntegerField(null=False)
    Env_fire10 = models.IntegerField(null=False)
    Env_fire11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EnvironmentalBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Env_fire_ball1 = models.IntegerField(null=False)
    Env_fire_ball2 = models.IntegerField(null=False)
    Env_fire_ball3 = models.IntegerField(null=False)
    Env_fire_ball4 = models.IntegerField(null=False)
    Env_fire_ball5 = models.IntegerField(null=False)
    Env_fire_ball6 = models.IntegerField(null=False)
    Env_fire_ball7 = models.IntegerField(null=False)
    Env_fire_ball8 = models.IntegerField(null=False)
    Env_fire_ball9 = models.IntegerField(null=False)
    Env_fire_ball10 = models.IntegerField(null=False)
    Env_fire_ball11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)
