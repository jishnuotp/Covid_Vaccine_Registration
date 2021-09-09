# Generated by Django 3.2.6 on 2021-08-24 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine_Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.district')),
            ],
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=40)),
                ('Age', models.IntegerField(blank=True)),
                ('Email', models.TextField(blank=True)),
                ('Contact_Number', models.TextField(max_length=10)),
                ('Address', models.TextField(blank=True)),
                ('District', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Registration.district')),
                ('Vaccine_Center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Registration.vaccine_center')),
            ],
        ),
    ]
