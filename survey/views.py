from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Survey, Field, MultipleChoice
from .forms import SurveyForm, FieldForm, FieldModelFormset, ChoiceForm, ChoiceIssueForm


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

    return render(request, 'survey/make_field_txt.html', {
        'field': form,
    })


def make_field_mul(request, pk):
    field = get_object_or_404(Field, pk=pk)
    try:
        selected_choice = field.multiplechoice_set.get(pk=request.POST['multiple_choice'])
    except (KeyError, MultipleChoice.DoesNotExist):
        return render(request, 'survey/make_field_mul.html', {'field': field,
                                                               'error_message':
                                                               "You didn't select a choice", })
    else:
        selected_choice += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('survey:results', args=field.id,))


def make_field_txt(request, pk):
    field = get_object_or_404(Field, pk=pk)
    try:
        text_answer = field.textanswer_set.all()
    except (KeyError, text_answer.DoesNotExist):
        return render(request, 'survey/make_field_txt.html', {'field': field,
                                                               'error_message':
                                                               "You didn't write answer", })
    else:
        return redirect('survey:make_index', field.pk)


def results(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, 'survey/results.html', {'field': field})


# def make_field_new(request, pk):
#     if request.method == 'POST':
#         formset = FieldModelFormset(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data.get('question'):
#                     form.save(commit=False)
#                     form.survey = Survey.objects.get(pk=pk)
#                     form.save()
#             return redirect('root')
#     else:
#         formset = FieldModelFormset(queryset=Field.objects.none())
#     return render(request, 'survey/make_index.html', {
#         'formset': formset,
#     })

ChoiceFormSet = formset_factory(ChoiceForm, ChoiceIssueForm, can_order=True, can_delete=True, extra=0)
def this_is_test(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        choiceformset = ChoiceFormSet(request.POST)

        if form.is_valid() and choiceformset.is_valid():
            form.save()
            choiceformset.save()
        return redirect('survey:make_index')
    else:
        form = ChoiceForm()
        data = {
            'form-TOTAL_FORMS' : '1',
            'form-INITIAL_FORMS' : '1',
            'form-MAX_NUM_FORMS': '10',
        }
        choiceformset = ChoiceFormSet(data)
    return render(request, 'survey/test.html', {
        'form': form,
        'choiceformset': choiceformset,
    })
