from django.db import models
from django_countries.fields import CountryField
from meta.models import ModelMeta

from pyconbalkan.core.models import SingleActiveModel
from markdownx.models import MarkdownxField


class Conference(SingleActiveModel, ModelMeta):
    INTERNATIONAL = 0
    NATIONAL = 1
    CONF_TYPE = (
        (INTERNATIONAL, 'International'),
        (NATIONAL, 'National'),
    )

    event = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(null=True, blank=True, max_length=100)
    year = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    city = models.CharField(null=True, blank=True, max_length=200)
    country = CountryField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    type = models.IntegerField(choices=CONF_TYPE)
    sponsor_email = models.EmailField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    # Links
    tickets = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    # timetable
    timetable_pdf = models.FileField(blank=True, null=True)


    _metadata = {
        'title': 'get_meta_title',
        'description': 'get_meta_description',
    }

    def get_meta_title(self):
        return '#{} {} {} {}'.format(self.number, self.event, self.name, self.year)

    def get_meta_description(self):
        return 'Welcome to {} {} {}! '.format(self.event, self.name, self.year)

    def __str__(self):
        return '{} {} {}'.format(self.event, self.name, self.year)


class CountDown(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    count_down = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class MissionStatement(SingleActiveModel):
    content = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.content
