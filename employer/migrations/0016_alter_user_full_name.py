# Generated by Django 4.1.3 on 2022-12-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0015_alter_user_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Anonymous', max_length=80),
        ),
    ]
