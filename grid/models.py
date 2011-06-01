from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Grid(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _('Grid')
        verbose_name_plural = _('Grids')

    def __unicode__(self):
        return self.name


class Feature(models.Model):
    grid = models.ForeignKey(Grid, verbose_name=_('Grid'))
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    ordering = models.PositiveIntegerField(_('Ordering'), default=0)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')
        ordering = ['ordering', 'id']

    def __unicode__(self):
        return self.name


class Element(models.Model):
    feature = models.ForeignKey(Feature, verbose_name=_('Feature'))
    text = models.TextField(_('Text'), blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Element')
        verbose_name_plural = _('Elements')
        ordering = []

    def __unicode__(self):
        return self.text

