# Generated by Django 5.1.7 on 2025-04-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_alter_songs_tune_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='tune_type',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Jig', 'Jig'), ('Reel', 'Reel'), ('Polka', 'Polka'), ('Listening Tune', 'Listening_Tune')], max_length=25),
        ),
    ]
