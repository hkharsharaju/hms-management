# Generated by Django 3.0 on 2023-09-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0013_roomfee'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_field', models.DateField()),
            ],
        ),
    ]