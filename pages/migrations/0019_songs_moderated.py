# Generated by Django 5.1.7 on 2025-04-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_customuser_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='moderated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
