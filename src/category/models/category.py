from typing import Tuple

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Category(BaseModel):
    CATEGORY_TYPES: Tuple = (
        ('DEVICE', _('device', ), ),
        ('GARMENTS', _('garments', ), ),
        ('ACCESSORIES', _('accessories', ), ),
    )
    name = models.CharField(max_length=150, )
    image = models.TextField(null=True, blank=True, )
    type = models.CharField(max_length=20, choices=CATEGORY_TYPES, default='DEVICE', )
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        db_table = 'categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
