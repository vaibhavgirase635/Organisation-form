# Generated by Django 4.2.1 on 2023-05-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_customuser_is_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(default=False, null=True, verbose_name='Is_employee'),
        ),
    ]
