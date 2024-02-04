from django import forms

from invitation_manager.models.guest import Entourage, Guest


class GuestInfoForm(forms.ModelForm):
    class Meta:
        fields = ["overnight_stay", "food_preferences", "note"]
        model = Guest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["food_preferences"].label = "Besondere Essenswünsche"
        self.fields["overnight_stay"].label = "Ich möchte übernachten"
        self.fields["overnight_stay"].widget = forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
        self.fields["note"].label = "Möchtest du noch etwas ergänzen?"


class EntourageForm(forms.ModelForm):
    class Meta:
        fields = ["display_name", "food_preferences", "overnight_stay"]
        model = Entourage

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["display_name"].label = "Name"
        self.fields["display_name"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["food_preferences"].label = "Besondere Essenswünsche"
        self.fields["overnight_stay"].label = "Mit Übernachtung"
        self.fields["overnight_stay"].widget = forms.CheckboxInput(
            attrs={"class": "form-check-input"}
        )
