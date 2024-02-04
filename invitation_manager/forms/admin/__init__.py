from django import forms
from django.contrib.auth.models import User

from invitation_manager.models.guest import Guest


class GuestAdminForm(forms.ModelForm):
    display_name = forms.CharField(required=True)

    class Meta:
        fields = "__all__"
        model = Guest

    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']

        if not self.instance.id and User.objects.filter(username=display_name).exists():
            raise forms.ValidationError("Dieser Benutzername ist bereits vergeben.")

        return display_name
