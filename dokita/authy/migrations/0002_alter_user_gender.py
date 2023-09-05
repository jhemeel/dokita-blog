# Generated by Django 4.2.4 on 2023-08-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('', 'Do not wish to disclose')], default='M', max_length=2),
        ),
    ]
