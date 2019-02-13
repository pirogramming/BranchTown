from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.HiddenInput(), initial='123')
    address = forms.CharField(widget=forms.HiddenInput(), initial='123')
    occupation = forms.CharField(widget=forms.HiddenInput(), initial='123')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()

        Profile.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            occupation = self.cleaned_data['occupation'],
        )
        return user


class SignupForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['phone_number', 'address', 'occupation']
