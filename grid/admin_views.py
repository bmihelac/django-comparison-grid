from django.template import RequestContext
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from grid.models import Grid, Feature, Element
from grid.admin_forms import ElementForm


def grid(request, object_id, **kwargs):
    ctx = RequestContext(request, {
        'app_label': Grid._meta.app_label,
        'opts': Grid._meta,
        })
    grid = get_object_or_404(Grid, pk=object_id)
    ctx['grid'] = grid
    return render_to_response('admin/grid/grid/edit_grid.html', ctx)


def edit_element(request, object_id, feature_id, content_type_id, item_id, **kwargs):
    ctx = RequestContext(request, {
        'app_label': Grid._meta.app_label,
        'opts': Grid._meta,
        })
    grid = get_object_or_404(Grid, pk=object_id)
    feature = get_object_or_404(Feature, pk=feature_id)
    item_type = ContentType.objects.get(pk=content_type_id)
    item = get_object_or_404(item_type.model_class(), pk=item_id)

    try:
        instance = Element.objects.get(feature=feature,
                content_type=item_type,
                object_id=item.id)
    except Element.DoesNotExist:
        instance = Element(feature=feature, content_object=item)

    if request.POST:
        form = ElementForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, _('Grid element saved.'))
            return redirect("admin:grid_grid_edit_grid", object_id=grid.id)
    else:
        form = ElementForm(instance=instance)
    ctx['grid'] = grid
    ctx['form'] = form
    ctx['feature'] = feature
    ctx['item'] = item
    template_names = ['admin/grid/grid/element_form.html']
    return render_to_response(template_names, ctx)

