from django.contrib import admin

from .models.content import Content, ImageFile
from .models.guest import Guest, Entourage


class EntourageInline(admin.TabularInline):
    model = Entourage
    extra = 0


class GuestAdmin(admin.ModelAdmin):
    inlines = [EntourageInline]
    readonly_fields = ['link_identifier']


class ImageFileInline(admin.TabularInline):
    model = ImageFile
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageFileInline]


# Register your models here.
admin.site.register(Guest, GuestAdmin)
admin.site.register(Content, ContentAdmin)
