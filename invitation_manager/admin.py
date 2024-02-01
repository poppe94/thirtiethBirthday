from django.contrib import admin

from .models import Guest, Entourage


class EntourageInline(admin.TabularInline):
    model = Entourage
    extra = 0


class GuestAdmin(admin.ModelAdmin):
    inlines = [EntourageInline]
    readonly_fields = ['link_identifier']


# Register your models here.
admin.site.register(Guest, GuestAdmin)
