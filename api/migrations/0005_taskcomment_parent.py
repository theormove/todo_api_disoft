# Generated by Django 4.1.5 on 2023-03-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task_asignees_alter_task_author_alter_task_edited_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='api.taskcomment'),
        ),
    ]
