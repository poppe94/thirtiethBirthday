from django import forms

from invitation_manager.models.guest import Entourage, Guest


class GuestInfoForm(forms.ModelForm):
    class Meta:
        fields = ["overnight_stay", "food_preferences", "note"]
        model = Guest
        widgets = {
            "overnight_stay": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "food_preferences": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["food_preferences"].label = "Besondere Essenswünsche"
        self.fields["overnight_stay"].label = "Ich möchte übernachten"
        self.fields["note"].label = "Möchtest du noch etwas ergänzen?"


class EntourageForm(forms.ModelForm):
    class Meta:
        fields = ["display_name", "food_preferences", "overnight_stay"]
        model = Entourage
        widgets = {
            "display_name": forms.TextInput(attrs={"class": "form-control"}),
            "food_preferences": forms.Select(attrs={"class": "form-select"}),
            "overnight_stay": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["display_name"].label = "Name"
        self.fields["food_preferences"].label = "Besondere Essenswünsche"
        self.fields["overnight_stay"].label = "Mit Übernachtung"
