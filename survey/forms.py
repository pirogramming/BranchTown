from django import forms
from django.forms import modelformset_factory, formset_factory

from tag.models import Tag
from .models import Survey, Field, MultipleChoice


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title', 'subtitle',)

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(), )

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['tags'] = [t.pk for t in kwargs['instance'].tag_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        # Get the unsave Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.tag_set.clear()
            instance.tag_set.add(*self.cleaned_data['tags'])

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance




class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('question',)   # 'type',


ChoiceFormSet = modelformset_factory(
    MultipleChoice,
    fields=['choice_text'],
    extra=1,
    widgets={
        'choice_text': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter choice text',
            }
        )
    }
)
