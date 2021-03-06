# Generated by Django 3.1.2 on 2020-11-07 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='D:\\Coding\\Hackathons\\ITFest_2020\\backend\\media/users/default.png', upload_to='D:\\Coding\\Hackathons\\ITFest_2020\\backend\\media/users'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
