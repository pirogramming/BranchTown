from django.shortcuts import render, redirect

from accounts.decorators import login_forbidden
from .forms import SignupForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_forbidden
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
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
