from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        print('custom')
        data = form.cleaned_data
        user.email = data.get('email')
        user.username = data.get('username')
        # all your custom fields
        #user.date_of_birth = data.get('date_of_birth')
        #ser.gender = data.get('gender')
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user