# Generated by Django 2.0.6 on 2018-06-12 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='numeto',
            new_name='numero',
        ),
    ]
