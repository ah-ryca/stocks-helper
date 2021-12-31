from django.db import models
from django_jalali.db import models as jmodels


class BaseModel(models.Model):
    """Abstract class for create automatically created_at and updated_at."""
    objects = jmodels.jManager()

    created_at = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = jmodels.jDateTimeField(auto_now=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
