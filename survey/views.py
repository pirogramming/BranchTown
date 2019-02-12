from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Survey
from .forms import SurveyForm, FieldForm


@login_required
def make_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('survey:make_field', form.pk)
    else:
        form = SurveyForm()

    return render(request, 'survey/make_survey.html', {
        'form': form,
    })


@login_required
def make_field(request, pk):
    if request.method == "POST":
        field = FieldForm(request.POST, request.FILES)
        if field.is_valid():
            field = field.save(commit=False)
            field.form = Survey.objects.get(pk=pk)
            field.save()
            return redirect('/board/')
    else:
        field = FieldForm()

    return render(request, 'survey/make_field.html', {
        'field': field,
    })


