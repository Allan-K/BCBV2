# Generated by Django 5.1.7 on 2025-05-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_dances_setlist_dance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dances',
            options={},
        ),
        migrations.AddField(
            model_name='setlist',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
