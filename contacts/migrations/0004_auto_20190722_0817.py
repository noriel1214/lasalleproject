# Generated by Django 2.2.3 on 2019-07-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190722_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
