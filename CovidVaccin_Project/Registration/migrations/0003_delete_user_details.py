# Generated by Django 3.2.6 on 2021-08-24 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_alter_user_details_first_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Details',
        ),
    ]