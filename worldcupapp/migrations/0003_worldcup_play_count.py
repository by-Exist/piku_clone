# Generated by Django 3.1.5 on 2021-01-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcupapp', '0002_auto_20210105_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcup',
            name='play_count',
            field=models.IntegerField(default=0, editable=False, verbose_name='플레이 횟수'),
        ),
    ]