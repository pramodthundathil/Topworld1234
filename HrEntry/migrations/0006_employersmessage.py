# Generated by Django 3.2.14 on 2022-11-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HrEntry', '0005_dropedresume'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployersMessage',
            fields=[
                ('EmpmassageID', models.AutoField(primary_key=True, serialize=False)),
                ('OrganasationName', models.CharField(max_length=255)),
                ('EmailID', models.CharField(max_length=255)),
                ('PhoneNumber', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
