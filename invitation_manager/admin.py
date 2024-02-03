from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse

from .forms.admin import GuestAdminForm
from .models.content import Content, ImageFile
from .models.guest import Guest, Entourage


class EntourageInline(admin.TabularInline):
    model = Entourage
    extra = 0


class GuestAdmin(admin.ModelAdmin):
    inlines = [EntourageInline]
    readonly_fields = ['link_identifier_url']
    exclude = ['user', 'link_identifier']
    form = GuestAdminForm

    def save_model(self, request, obj, form, change):
        if not change and not getattr(obj, 'user', None):
            new_user = User.objects.create_user(obj.display_name)
            obj.user = new_user

        super(GuestAdmin, self).save_model(request, obj, form, change)

    def link_identifier_url(self, obj):
        return reverse("link-identifier-auth", args=(obj.link_identifier,))


class ImageFileInline(admin.TabularInline):
    model = ImageFile
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageFileInline]


# Register your models here.
admin.site.register(Guest, GuestAdmin)
admin.site.register(Content, ContentAdmin)
