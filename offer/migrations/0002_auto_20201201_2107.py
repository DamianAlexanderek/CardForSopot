# Generated by Django 3.1.3 on 2020-12-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='end_date',
            field=models.DateField(default=True),
        ),
    ]