from django.shortcuts import render, redirect

from accounts.decorators import login_forbidden
from .forms import SignupForm, SignupForm2
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.contrib.auth import login as dj_login



@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_forbidden
def signup(request):
    if request.method == 'POST':
        print('STEP1: print POST if this is a POST')
        form = SignupForm(request.POST)
        if form.is_valid():
            print('step1 form is valid.')
            user = form.save()
            print('SignupForm saved')
            dj_login(request, user, backend='django.contrib.auth.backends.ModelBackend')    # added
            print('redirecting...')
            return redirect('../signup2/')    # redirect(settings.LOGIN_URL)
        else:
            print("request is invalid: {}".format(request.POST))
            return "bad request!", 500
    else:
        print('STEP1: print GET if this is a GET')
        form = SignupForm()

        return render(request, 'accounts/signup_form.html', {
            'form': form,
        })



def signup2(request):
    init_profile = request.user.profile
    if request.method == 'POST':
        print('STEP2: print POST if this is a POST')
        form = SignupForm2(request.POST, instance=init_profile)
        if form.is_valid():
            print('step2 form is valid.')
            form.save()
            return redirect(settings.LOGIN_URL)
        else:
            print("request is invalid: {}".format(request.POST))
            return "bad request!", 500
    else:
        print('STEP2: print GET if this is a GET')
        form = SignupForm2()
        return render(request, 'accounts/signup_form2.html', {
            'form': form,
        })




@login_forbidden
def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return LoginView.as_view(template_name="accounts/login_form.html", extra_context={'providers': providers})(request)


