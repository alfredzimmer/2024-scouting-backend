# Generated by Django 4.2.10 on 2024-02-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouting', '0004_record_strategy_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='cycle_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
