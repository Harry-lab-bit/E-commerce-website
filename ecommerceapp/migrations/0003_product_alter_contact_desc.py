# Generated by Django 4.2 on 2024-12-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_alter_contact_email_alter_contact_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images/images')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
