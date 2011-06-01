from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from grid.models import Element


register = template.Library()


@register.filter
def grid_feature(item, feature):
    try:
        val = Element.objects.get(feature=feature, 
                content_type=ContentType.objects.get_for_model(item),
                object_id=item.id)
    except Element.DoesNotExist:
        val = ""
    return val

@register.simple_tag
def edit_element_url(feature, item):
    return reverse('admin:grid_grid_edit_element',
            args=(feature.grid.id, feature.id,
                ContentType.objects.get_for_model(item).id, item.id))
