import django_tables2 as tables

from images.models import Image


class ImageTable(tables.Table):

    class Meta:
        model = Image
        orderable = False
