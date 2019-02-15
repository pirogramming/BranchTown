from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Survey, Field, MultipleChoice
from .forms import SurveyForm, FieldForm


@login_required
def make_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.save()
            return redirect('survey:make_index', survey.pk)
    else:
        form = SurveyForm()

    return render(request, 'survey/make_survey.html', {
        'form': form,
    })


@login_required
def make_index(request, pk):
    survey = Survey.objects.get(pk=pk)
    field_list = Survey.objects.get(pk=pk).field_set.all()
    context = {
        'survey': survey,
        'field_list': field_list,
    }
    return render(request, 'survey/make_index.html', context)


@login_required
def make_field(request, pk):
    if request.method == "POST":
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            field = form.save(commit=False)
            field.survey = Survey.objects.get(pk=pk)
            field.save()
            return redirect('/board/')
    else:
        form = FieldForm()

    return render(request, 'survey/make_field.html', {
        'field': form,
    })


def multiple_choice(request, pk):
    field = get_object_or_404(Field, pk=pk)
    try:
        selected_choice = field.multiplechoice_set.get(pk=request.POST['multiple_choice'])
    except (KeyError, MultipleChoice.DoesNotExist):
        return render(request, 'survey/multiple_choice.html', {'field': field,
                                                               'error_message':
                                                               "You didn't select a choice", })
    else:
        selected_choice += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('survey:results', args=field.id,))


def results(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, 'survey/results.html', {'field': field})
