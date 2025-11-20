from django.contrib.admin import register

from base.admin import NoDeleteActionModelAdmin
from meetings.models import Meeting, Guest


@register(Meeting)
class MeetingAdmin(NoDeleteActionModelAdmin):
    pass


@register(Guest)
class GuestAdmin(NoDeleteActionModelAdmin):
    pass
