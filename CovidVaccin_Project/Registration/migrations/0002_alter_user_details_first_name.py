# Generated by Django 3.2.6 on 2021-08-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='First_Name',
            field=models.CharField(max_length=250),
        ),
    ]
