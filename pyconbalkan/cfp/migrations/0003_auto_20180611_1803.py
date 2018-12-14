# Generated by Django 2.0.5 on 2018-06-11 18:03
import random
import string

from django.db import migrations, models
from slugify import slugify


def create_slug_in_cfp(apps, schema_editor):
    # Create slug in Cfp
    Cfp = apps.get_model("cfp", "Cfp")
    for cfp in Cfp.objects.all():
        cfp.slug = '{}-{}'.format(slugify(cfp.title), ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))
        cfp.accepted = False
        cfp.save()

def remove_slug(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0002_auto_20180604_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='cfp',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cfp',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
            ),
        migrations.RunPython(create_slug_in_cfp, remove_slug)
    ]
