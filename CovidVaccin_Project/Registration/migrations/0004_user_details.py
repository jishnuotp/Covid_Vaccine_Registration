# Generated by Django 3.2.6 on 2021-08-24 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_delete_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=250)),
                ('Last_name', models.CharField(max_length=40)),
                ('Email', models.TextField()),
                ('Address', models.TextField()),
                ('Contact_Number', models.IntegerField(max_length=10)),
                ('Age', models.IntegerField(max_length=3)),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.district')),
                ('Vaccine_Center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.vaccine_center')),
            ],
        ),
    ]
