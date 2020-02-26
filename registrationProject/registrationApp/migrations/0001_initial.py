# Generated by Django 2.2.10 on 2020-02-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_registraion_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(unique=True)),
                ('emp_username', models.CharField(max_length=100)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_age', models.IntegerField()),
                ('emp_gender', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_mobile', models.BigIntegerField()),
                ('emp_password', models.CharField(max_length=100)),
            ],
        ),
    ]
