from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from base.models import BaseModel


class Meeting(BaseModel):
    PLANNED = "P"
    CANCELED = "C"
    FINISHED = "F"
    STATUS_CHOICES = [
        (PLANNED, "Planned"),
        (CANCELED, "Canceled"),
        (FINISHED, "Finished"),
    ]

    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    topic = models.CharField(max_length=100)
    notes = models.TextField(blank=True, default="")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PLANNED)
    participant_name = models.CharField(max_length=300)
    participant_email = models.EmailField()

    def __str__(self) -> str:
        return f"({self.start_time.date()}) {self.topic}"

    def clean(self):
        super().clean()
        if self.start_time >= self.end_time:
            raise ValidationError("Meeting start time must be before end time.")


class Guest(BaseModel):
    email = models.EmailField()
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("email", "meeting")

    def __str__(self) -> str:
        return f"{self.email}"
