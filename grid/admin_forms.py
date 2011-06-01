from django.forms import ModelForm

from grid.models import Element


class ElementForm(ModelForm):

    class Meta:
        model = Element
        fields = ('text', )

