from django import forms
from django.forms import modelformset_factory

from .models import Survey, Field


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'subtitle', 'tag', 'status']


FieldModelFormset = modelformset_factory(
    Field,
    fields=('survey', 'type', 'question'),
    extra=1,
    widgets={
        'type': forms.CharField(),
        'question': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'write question'
        })
    }
)


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['type', 'question']


