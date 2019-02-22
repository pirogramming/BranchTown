from django import forms
from django.forms import modelformset_factory

from survey.models import TextAnswer


TextAnswerFormSet = modelformset_factory(
    TextAnswer,
    fields=['answer'],
    widgets={
        'answer': forms.Textarea(
            attrs={
                # 'class': 'form-control',
                'placeholder': 'Enter your answer',
            }
        )
    }
)


class TextAnswerForm(forms.ModelForm):
    class Meta:
        model = TextAnswer
        fields = ['field', 'answer']
