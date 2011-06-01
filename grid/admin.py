from django.contrib import admin
from django.conf.urls.defaults import patterns, url

from grid.models import Grid, Feature
from grid.admin_views import grid, edit_element


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 0


class GridAdmin(admin.ModelAdmin):
    inlines = (FeatureInline, )

    def get_urls(self):
        urls = super(GridAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^(?P<object_id>\d+)/grid/$',
                self.admin_site.admin_view(grid),
                name="grid_grid_edit_grid"),
            url(r'^(?P<object_id>\d+)/grid/(?P<feature_id>\d+)/(?P<content_type_id>\d+)/(?P<item_id>\d+)/$',
                self.admin_site.admin_view(edit_element),
                name="grid_grid_edit_element"),
        )
        return my_urls + urls


admin.site.register(Grid, GridAdmin)
