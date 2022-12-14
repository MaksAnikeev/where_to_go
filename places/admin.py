from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin

from .admin_functions import preview
from .models import Image, Place


class ImageTabularInline(SortableStackedInline):
    model = Image
    fields = ['img', 'preview', 'number']
    ordering = ['number']
    readonly_fields = ['preview']
    preview = preview


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageTabularInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'number', 'preview')
    fields = ['place', 'number', 'img', 'preview', ]
    raw_id_fields = ('place',)
    readonly_fields = ['preview']
    preview = preview

