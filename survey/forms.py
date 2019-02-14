from django import forms
from .models import Survey, Field


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'subtitle']


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['type', 'question']


