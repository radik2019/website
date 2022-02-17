# Generated by Django 4.0.2 on 2022-02-16 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0004_alter_electronics_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='electronics',
            name='content',
            field=models.TextField(unique=True),
        ),
        migrations.AddField(
            model_name='electronics',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='electronics.category'),
        ),
    ]