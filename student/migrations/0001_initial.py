# Generated by Django 3.1.1 on 2020-10-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('spass', models.CharField(max_length=100)),
            ],
        ),
    ]
