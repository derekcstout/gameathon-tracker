# Generated by Django 3.1.3 on 2020-11-10 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameboard', '0002_playergameboard'),
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Awards',
            new_name='Award',
        ),
    ]