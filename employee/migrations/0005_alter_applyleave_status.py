# Generated by Django 4.1.3 on 2022-12-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_applyleave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyleave',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
    ]
