# Generated by Django 4.2.1 on 2023-05-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_customuser_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]