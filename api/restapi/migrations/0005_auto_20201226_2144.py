# Generated by Django 3.1.4 on 2020-12-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_member_temp_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(db_index=True, max_length=15),
        ),
    ]
