# Generated by Django 2.0.5 on 2018-08-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0006_sponsoring_organization_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsoring',
            name='level',
            field=models.CharField(choices=[('Keystone', 'keystone'), ('Platinum', 'platinum'), ('Gold', 'gold'), ('Silver', 'silver'), ('Partner', 'partner')], default='Partner', max_length=16),
        ),
    ]
