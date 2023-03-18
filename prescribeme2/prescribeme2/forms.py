from django import forms
from prescribeme2.models import Premodel


class Preforms(forms.ModelForm):
    class Meta:
        model = Premodel
        fields = "__all__"
