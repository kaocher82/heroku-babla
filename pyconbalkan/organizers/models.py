from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from pyconbalkan.core.models import Person, ActiveModel


class Volunteer(ActiveModel, Person):
    ORGANIZER = 0
    VOLUNTEER = 1
    VOLUNTEER_TYPE = (
        (ORGANIZER, 'Organizer'),
        (VOLUNTEER, 'Volunteer'),
    )

    user = models.OneToOneField(User, blank=True, null=True, related_name='volunteer', on_delete=CASCADE)
    type = models.IntegerField(choices=VOLUNTEER_TYPE, default=VOLUNTEER)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.get_type_display())

    class Meta:
        ordering = ('full_name',)


class VolunteerPhoto(models.Model):
    volunteer = models.ForeignKey(Volunteer, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="organizers/volunteer/profile_picture", blank=True)
