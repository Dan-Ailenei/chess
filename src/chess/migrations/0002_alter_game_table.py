# Generated by Django 4.1.4 on 2022-12-20 15:50

import chess.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='table',
            field=models.JSONField(default=chess.models.build_default_table),
        ),
    ]