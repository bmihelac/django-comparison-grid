======================
Django comparison grid
======================

`Comparison grid` django application allows creating comparison grids,
attaching arbitary content types to grids and editing
grid content through django admin interface.

Requiremenents
--------------

* Django 1.2 or later (please note that example app uses CBV available in 
  Django 1.3)

Configuration
-------------

Add ``grid`` to INSTALLED_APPS::

    INSTALLED_APPS = (

        'grid',
    )


Usage
-----

1. Add ``grids`` foreign field to models that you want to be connectable to
   grids, for example::

    class Product(models.Model):
        grids = models.ManyToManyField(Grid,
                related_name='grid_items',
                null=True,
                blank=True)

    ``Grid`` model expect related name to be set to ``grid_items``.

Example app
-----------

To test application and get a feeling how it works::

    cd example
    ./manage.py syncdb --noinput && ./manage.py loaddata sample_data.json
    ./manage.py runserver

Username is ``admin``. Password is ``password``.

TODO
----

* ajax editing

* allow ordering of grid items

* allow restricting by features or items in templatetag
