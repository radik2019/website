# Generated by Django 4.0.2 on 2022-02-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0006_rename_category_operatingsystem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatingsystem',
            name='name',
            field=models.CharField(db_index=True, max_length=40, unique=True),
        ),
    ]
