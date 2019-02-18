from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Survey, Field, MultipleChoice
from .forms import SurveyForm, FieldForm, TextAnswerForm, ChoiceFormSet


@login_required
def make_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.status = 'o'     # TODO: 일단 'o' 로 설정, 추후에 model 에 status 추가 후 값 변경해야함
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
    if request.user == survey.author:
        field_list = survey.field_set.all()
        context = {
            'survey': survey,
            'field_list': field_list,
        }
        return render(request, 'survey/make_index.html', context)
    else:
        return redirect('root')
        # TODO: 설문 작성자와 user 가 동일하지 않을 경우, 일단 root 로 redirect


def multiple_choice(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user == survey.author:
        if request.method == "POST":
            field_form = FieldForm(request.POST)
            formset = ChoiceFormSet(request.POST)
            if field_form.is_valid() and formset.is_valid():
                field = field_form.save(commit=False)
                field.survey = survey
                field.type = '2'
                field.save()
                for form in formset:
                    choice = form.save(commit=False)
                    choice.field = field
                    choice.save()
                return redirect('survey:make_index', pk)
        else:
            field_form = FieldForm()
            formset = ChoiceFormSet(queryset=MultipleChoice.objects.none())
        return render(request, 'survey/make_choice.html', {
            'field_form': field_form,
            'formset': formset,
        })
    else:
        return redirect('root')
        # TODO: 설문 작성자와 user 가 동일하지 않을 경우, 일단 root 로 redirect


def text_answer(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user == survey.author:
        if request.method == "POST":
            form = TextAnswerForm(request.POST)     # TODO: Field Form 과 차이점 X,
            if form.is_valid():
                field = form.save(commit=False)
                field.survey = survey
                field.type = '1'
                field.save()
                return redirect('survey:make_index', pk)
        else:
            form = TextAnswerForm()
        return render(request, 'survey/make_text_answer.html', {
            'survey': survey,
            'form': form,
        })
    else:
        return redirect('root')
        # TODO: 설문 작성자와 user 가 동일하지 않을 경우, 일단 root 로 redirect


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


# def multiple_choice(request, pk):
#     field = get_object_or_404(Field, pk=pk)
#     try:
#         selected_choice = field.multiplechoice_set.get(pk=request.POST['multiple_choice'])
#     except (KeyError, MultipleChoice.DoesNotExist):
#         return render(request, 'survey/multiple_choice.html', {'field': field,
#                                                                'error_message':
#                                                                "You didn't select a choice", })
#     else:
#         selected_choice += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('survey:results', args=field.id,))


def results(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, 'survey/results.html', {'field': field})
