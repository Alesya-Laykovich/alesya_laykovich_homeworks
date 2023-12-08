# Generated by Django 4.2.7 on 2023-11-28 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0006_alter_taskmanager_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmanager',
            name='user',
        ),
        migrations.AddField(
            model_name='taskmanager',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
