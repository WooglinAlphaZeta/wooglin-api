# Generated by Django 3.1.4 on 2021-01-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_auto_20210120_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoberBroShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of shift start')),
                ('time_start', models.DateTimeField(verbose_name='Shift start')),
                ('time_end', models.DateTimeField(verbose_name='Shift end')),
                ('capacity', models.IntegerField(default=5, verbose_name='The number of brothers who are able to sign up for this slot.')),
            ],
        ),
    ]