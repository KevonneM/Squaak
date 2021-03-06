# Generated by Django 4.0.4 on 2022-06-01 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateVideoChatRoom',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('online', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('videouser1', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='videouser1', to=settings.AUTH_USER_MODEL)),
                ('videouser2', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='videouser2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
