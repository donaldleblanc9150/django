# Generated by Django 2.2.4 on 2020-06-11 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0004_auto_20200610_0200'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]