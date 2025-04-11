# Generated by Django 5.2 on 2025-04-11 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('registry_date', models.DateField(default=datetime.date.today)),
                ('state', models.CharField(choices=[('1', 'tO DO'), ('2', 'Completed')], default='1', max_length=1)),
            ],
        ),
    ]
