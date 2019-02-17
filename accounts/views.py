from django.shortcuts import render, redirect

from accounts.decorators import login_forbidden
from accounts.models import Profile
from .forms import SignupForm2, CustomSignupForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.contrib.auth import login as dj_login

from django.contrib.auth.models import User as U



@login_required
def profile(request):
    print(request.user.profile.tag)
    return render(request, 'accounts/profile.html')


@login_forbidden    # TODO login 되어있는 상태에서 accounts/signup or accounts/signup2 url 들어가면 redirect to accounts/profile
def signup(request):
    if request.method == 'POST':
        print('STEP1: print POST if this is a POST')
        form = CustomSignupForm(request.POST, request.FILES)
        if form.is_valid():
            print('step1 form is valid.')
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if U.objects.filter(username=username).count():
                form.add_error('username', '이미 존재하는 닉네임입니다.')
            if U.objects.filter(email=email).count():
                form.add_error('email', '이미 존재하는 이메입니다.')

            else:
                request.session['step1_form'] = form.cleaned_data
                return redirect('../signup2/')

            context = {
                'form': form,
            }
            return render(request, 'accounts/signup_form.html', context=context)
        else:
            print("request is invalid: {}".format(request.POST))
            return "bad request!", 500
    else:
        print('STEP1: print GET if this is a GET')
        form = CustomSignupForm()

        return render(request, 'accounts/signup_form.html', {
            'form': form,
        })


@login_forbidden
def signup2(request):
    if request.method == 'POST':
        print('STEP2: print POST if this is a POST')
        form = SignupForm2(request.POST,)  # instance=init_profile)

        print('is it valid?')
        if form.is_valid():
            print('step2 form is valid.')
            # step1에서 받아온 정보 처
            step1_form = request.session.get('step1_form')
            username = step1_form['username']
            email = step1_form['email']
            pw = step1_form['pw1']
            profile = form.save(commit=False)
            user = U()
            user.email = email
            user.username = username
            user.first_name = step1_form['name'][1:]
            user.last_name = step1_form['name'][:1]
            user.set_password(pw)
            user.save()
            profile.user = user
            profile.save()

            receive_profile = Profile.objects.get(user_id=user.id)
            receive_profile.tag.add(*form.cleaned_data['tags'])

            context = {
                'form': form,
            }
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


