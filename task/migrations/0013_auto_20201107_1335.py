# Generated by Django 3.1.2 on 2020-11-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20201107_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.status'),
        ),
    ]
