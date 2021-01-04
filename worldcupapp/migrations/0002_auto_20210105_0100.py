# Generated by Django 3.1.5 on 2021-01-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldcupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31, verbose_name='제목')),
                ('image', models.ImageField(upload_to='worldcup/%Y/%m/%d/%h', verbose_name='이미지')),
                ('game_win_count', models.IntegerField(default=0, editable=False, verbose_name='월드컵 승리 횟수')),
                ('o2o_win_count', models.IntegerField(default=0, editable=False, verbose_name='1:1 승리 횟수')),
                ('world_cup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldcupapp.worldcup', verbose_name='월드컵')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]