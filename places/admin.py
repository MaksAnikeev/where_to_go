from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from django.contrib import admin

from .download_tools import preview
from .models import Image, Place


class ImageTabularInline(SortableStackedInline):
    model = Image
    fields = ['img', 'preview', 'number']
    ordering = ['number']
    readonly_fields = ['preview']
    preview = preview


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImageTabularInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'number', 'preview')
    fields = ['place', 'number', 'img', 'preview', ]
    raw_id_fields = ('place',)
    readonly_fields = ['preview']
    preview = preview

