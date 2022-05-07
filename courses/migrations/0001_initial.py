# Generated by Django 4.0.4 on 2022-05-07 03:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125, unique=True)),
                ('demo_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link_repo', models.CharField(max_length=125)),
            ],
        ),
    ]
