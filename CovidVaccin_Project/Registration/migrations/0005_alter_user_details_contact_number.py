# Generated by Django 3.2.6 on 2021-08-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='Contact_Number',
            field=models.TextField(max_length=10),
        ),
    ]