# Generated by Django 3.1.5 on 2021-01-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to='profile/%Y/%m/%d', verbose_name='아바타'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='message',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='소개글'),
            preserve_default=False,
        ),
    ]
