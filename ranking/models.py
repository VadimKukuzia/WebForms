from django.db import models

from user.models import User


# Create your models here.

# Economic
class EconomicBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EconomicFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EconomicBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


# Social
class SocialBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S1 = models.IntegerField(null=False)
    S2 = models.IntegerField(null=False)
    S3 = models.IntegerField(null=False)
    S4 = models.IntegerField(null=False)
    S5 = models.IntegerField(null=False)
    S6 = models.IntegerField(null=False)
    S7 = models.IntegerField(null=False)
    S8 = models.IntegerField(null=False)
    S9 = models.IntegerField(null=False)
    S10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class SocialFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S1 = models.IntegerField(null=False)
    S2 = models.IntegerField(null=False)
    S3 = models.IntegerField(null=False)
    S4 = models.IntegerField(null=False)
    S5 = models.IntegerField(null=False)
    S6 = models.IntegerField(null=False)
    S7 = models.IntegerField(null=False)
    S8 = models.IntegerField(null=False)
    S9 = models.IntegerField(null=False)
    S10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class SocialBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    S1 = models.IntegerField(null=False)
    S2 = models.IntegerField(null=False)
    S3 = models.IntegerField(null=False)
    S4 = models.IntegerField(null=False)
    S5 = models.IntegerField(null=False)
    S6 = models.IntegerField(null=False)
    S7 = models.IntegerField(null=False)
    S8 = models.IntegerField(null=False)
    S9 = models.IntegerField(null=False)
    S10 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


# Environmental
class EnvironmentalBlastShockWave(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)
    E11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EnvironmentalFire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)
    E11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)


class EnvironmentalBlastFireBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    E1 = models.IntegerField(null=False)
    E2 = models.IntegerField(null=False)
    E3 = models.IntegerField(null=False)
    E4 = models.IntegerField(null=False)
    E5 = models.IntegerField(null=False)
    E6 = models.IntegerField(null=False)
    E7 = models.IntegerField(null=False)
    E8 = models.IntegerField(null=False)
    E9 = models.IntegerField(null=False)
    E10 = models.IntegerField(null=False)
    E11 = models.IntegerField(null=False)

    adding_factors = models.TextField(max_length=255, null=True)
    additional_comment = models.TextField(max_length=512, null=True)
