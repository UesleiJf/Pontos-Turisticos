# Generated by Django 2.0.6 on 2018-06-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('numeto', models.IntegerField()),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
    ]
