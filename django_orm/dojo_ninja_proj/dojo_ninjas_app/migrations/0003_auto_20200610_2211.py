# Generated by Django 2.2.4 on 2020-06-10 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojos_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dojos',
            old_name='name',
            new_name='dojo_name',
        ),
    ]
