# Generated by Django 4.2 on 2024-04-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobBoard_app', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tools',
            field=models.CharField(blank=True, choices=[('Lawn Mower', 'LAWN MOWER'), ('shovel', 'SHOVEL')], max_length=200),
        ),
    ]
