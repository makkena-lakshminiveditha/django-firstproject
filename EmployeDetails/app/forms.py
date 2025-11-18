from django import forms

from app.models import employe_model
class employe_from(forms.ModelForm):
    class Meta:
        model = employe_model
        fields = '__all__'