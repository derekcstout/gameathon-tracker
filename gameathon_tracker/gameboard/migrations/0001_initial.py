# Generated by Django 3.1.3 on 2020-11-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gameboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameboard_name', models.CharField(max_length=200)),
                ('gameboard_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
