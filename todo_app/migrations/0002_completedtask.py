# Generated by Django 5.0.4 on 2024-04-16 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompletedTask', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo_app.tasks')),
            ],
        ),
    ]