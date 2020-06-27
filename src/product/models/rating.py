from django.db import models

from core.models import BaseModel


class ProductRating(BaseModel):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, )
    count = models.IntegerField()
    value = models.DecimalField(max_digits=2, decimal_places=1, )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'rating'
