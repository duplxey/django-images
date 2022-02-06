import django_tables2 as tables

from images.models import Image


class ImageTable(tables.Table):
    preview = tables.TemplateColumn('<img src="{{record.file.url}}" class="img-fluid" height="25" width="25">')

    class Meta:
        model = Image
        orderable = False
