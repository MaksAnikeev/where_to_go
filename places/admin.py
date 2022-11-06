from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html, mark_safe


class ImageInline(admin.TabularInline):
  model = Image
  fields = ['img', 'preview', 'number']
  readonly_fields = ['preview']

  def preview(self, obj):
    return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['place', 'number', 'img', 'preview', ]
    raw_id_fields = ('place', )
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')
