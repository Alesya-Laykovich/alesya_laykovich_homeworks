# Generated by Django 4.2.7 on 2023-11-28 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0005_taskmanager_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanager',
            name='user',
            field=models.ManyToManyField(default=True, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
