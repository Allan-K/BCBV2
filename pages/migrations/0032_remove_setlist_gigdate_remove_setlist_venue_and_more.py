# Generated by Django 5.1.7 on 2025-06-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_setlist_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setlist',
            name='gigdate',
        ),
        migrations.RemoveField(
            model_name='setlist',
            name='venue',
        ),
        migrations.AddField(
            model_name='set',
            name='venue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
