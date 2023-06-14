from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        username = email[:email.index('@')]
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255, unique=False)

    sex = models.CharField(default='M')
    age = models.IntegerField(default=1)
    income = models.IntegerField(default=1)
    marital_status = models.IntegerField(default=1)
    children_status = models.IntegerField(default=1)
    education = models.IntegerField(default=1)
    degree = models.IntegerField(default=1)
    driving_experience = models.IntegerField(default=1)
    # education_direction = ?
    technical_education_direction = models.BooleanField(default=False)
    economical_education_direction = models.BooleanField(default=False)
    environmental_education_direction = models.BooleanField(default=False)
    humanitarian_education_direction = models.BooleanField(default=False)
    working_organization = models.IntegerField(default=1)
    district = models.IntegerField(default=1)
    petrol_station_nearby = models.IntegerField(default=1)
    dwelling = models.IntegerField(default=1)

    email = models.EmailField(max_length=100, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
