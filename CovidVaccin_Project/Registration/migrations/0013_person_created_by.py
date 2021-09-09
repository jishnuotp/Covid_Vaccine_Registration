# Generated by Django 3.2.6 on 2021-09-05 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registration', '0012_remove_person_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]