# Generated by Django 2.2.4 on 2020-06-09 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
