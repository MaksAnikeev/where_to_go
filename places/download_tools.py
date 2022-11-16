from django.utils.html import format_html


def preview(self, obj):
    return format_html(
        '<img src="{url}" style="max-height: 200px;">',
        url=obj.img.url
        )
