# Generated by Django 4.1.5 on 2023-03-19 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_alter_task_asignees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='asignees',
            field=models.ManyToManyField(blank=True, null=True, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
