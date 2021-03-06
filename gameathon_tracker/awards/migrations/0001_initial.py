# Generated by Django 3.1.3 on 2020-11-16 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gameboard', '0003_gameboard_gameboard_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('team_game', models.BooleanField()),
                ('points_awarded', models.IntegerField()),
                ('award_created_at', models.DateTimeField()),
                ('player_gameboard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameboard.playergameboard')),
            ],
        ),
    ]
