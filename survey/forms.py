from django import forms
from .models import Survey, Question, Choice


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'subtitle']  # , 'author']




