# Generated by Django 4.2.2 on 2023-06-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='children_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='driving_experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='dwelling',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='income',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='petrol_station_nearby',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='M'),
        ),
        migrations.AlterField(
            model_name='user',
            name='working_organization',
            field=models.IntegerField(default=1),
        ),
    ]
