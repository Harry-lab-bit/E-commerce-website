# Generated by Django 4.2 on 2024-12-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default=True, max_length=254)),
                ('desc', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField(max_length=15)),
            ],
        ),
    ]
