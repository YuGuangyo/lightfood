# Generated by Django 3.2 on 2022-10-10 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='stu_integral',
            field=models.IntegerField(default=0, null=True),
        ),
    ]