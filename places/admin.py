from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableStackedInline, SortableAdminMixin


class ImageTabularInline(SortableStackedInline):
  model = Image
  fields = ['img', 'preview', 'number']
  ordering = ['number']
  readonly_fields = ['preview']

  def preview(self, obj):
    return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImageTabularInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'number', 'preview')
    fields = ['place', 'number', 'img', 'preview', ]
    raw_id_fields = ('place', )
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')
