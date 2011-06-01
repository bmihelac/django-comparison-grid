from django.db import models

from grid.models import Grid


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    grids = models.ManyToManyField(Grid,
            related_name='grid_items',
            null=True,
            blank=True)

    def __unicode__(self):
        return self.name

