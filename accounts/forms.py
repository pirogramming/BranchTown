from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from tag.models import Tag
from .models import Profile


# class SignupForm(UserCreationForm):
#     phone_number = forms.CharField(widget=forms.HiddenInput(), initial='123')
#     address = forms.CharField(widget=forms.HiddenInput(), initial='123')
#     occupation = forms.CharField(widget=forms.HiddenInput(), initial='123')
#
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ('email',)
#
#     def save(self):
#         user = super().save()
#
#         Profile.objects.create(
#             user=user,
#             phone_number=self.cleaned_data['phone_number'],
#             address=self.cleaned_data['address'],
#             occupation = self.cleaned_data['occupation'],
#         )
#         return user


class CustomSignupForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '닉네임'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'}))
    pw1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))
    pw2 = forms.CharField(label='',
                          widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 재입력'}))

    def clean(self):
        pw1 = self.cleaned_data['pw1']
        pw2 = self.cleaned_data['pw2']

        if pw1 == pw2:
            self.cleaned_data['pw'] = pw1
        else:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    class Meta:
        model = Profile
        fields = ('name', 'username', 'email', 'pw1', 'pw2', )  # 'region', 'phone')




class SignupForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['phone_number', 'address', 'occupation']

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

    # 소셜 로그인 후 추가 정보 입력 받아서 profile 생성
    def signup(self, request, user):
        print(request.POST)
        # profile = self.save(commit=False)
        #user = U()
        user.email = request.POST['email']
        user.username = request.POST['username']
        # user.first_name = step1_form['name'][1:]
        # user.last_name = step1_form['name'][:1]
        # user.set_password(pw)
        user.save()
        profile = Profile.objects.create(user=user, address = request.POST['address'], phone_number = request.POST['phone_number'], occupation = request.POST['occupation'])

        #profile.user = user
        # profile.address = request.POST['address']
        # profile.phone_number = request.POST['phone_number']
        # profile.occupation = request.POST['occupation']
        profile.save()

        receive_profile = Profile.objects.get(user_id=user.id)
        receive_profile.tag.add(*self.cleaned_data['tags'])



