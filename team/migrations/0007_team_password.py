# Generated by Django 3.1.2 on 2020-11-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_remove_team_passwords'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='password',
            field=models.CharField(default='ss', max_length=20),
            preserve_default=False,
        ),
    ]
