# Generated by Django 4.0.6 on 2022-12-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_alter_employeemodel_emp_id_alter_user_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='profile_pic/admin.png', upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='profile',
            field=models.ImageField(blank=True, default='profile_pic/admin.png', upload_to='profile_pic'),
        ),
    ]