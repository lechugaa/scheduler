from django.db import models


class BaseModel(models.Model):
    """
    BaseModel provides a core foundation for other models to inherit standardized
    fields for timestamp tracking.

    This class is designed to serve as an abstract model that includes `created_at`
    and `updated_at` fields for tracking the creation and modification timestamps
    of derived model instances.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
