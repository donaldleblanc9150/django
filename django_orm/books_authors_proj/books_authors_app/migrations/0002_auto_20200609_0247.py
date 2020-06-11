# Generated by Django 2.2.4 on 2020-06-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='desc',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
