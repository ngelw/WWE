# Generated by Django 5.1.2 on 2024-10-29 21:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royalrumble', '0002_wrestlers_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrestlers',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wrestler', to=settings.AUTH_USER_MODEL),
        ),
    ]
