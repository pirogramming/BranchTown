from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey, Field, MultipleChoice
from .forms import SurveyForm, FieldForm, ChoiceFormSet

@login_required
def make_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.status = 'o'     # TODO: 일단 'o' 로 설정, 추후에 model 에 status 추가 후 값 변경해야함
            survey.save()
            survey_instance = Survey.objects.get(pk=survey.pk)
            survey_instance.tag.add(*form.cleaned_data['tags'])
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


def make_multiple_choice(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user == survey.author:
        if request.method == "POST":
            field_form = FieldForm(request.POST)
            formset = ChoiceFormSet(request.POST)
            if field_form.is_valid() and formset.is_valid():
                field = field_form.save(commit=False)
                field.survey = survey
                field.type = '1'
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



def make_text_answer(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user == survey.author:
        if request.method == "POST":
            form = FieldForm(request.POST)     # TODO: Field Form 과 차이점 X,
            if form.is_valid():
                field = form.save(commit=False)
                field.survey = survey
                field.type = '3'
                field.save()
                return redirect('survey:make_index', pk)
        else:
            form = FieldForm()
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

    return render(request, 'survey/make_field_txt.html', {
        'field': form,
    })



def multiple_choice(request, pk):
    if request.method == "POST":
        choiceformset = ChoiceFormSet(request.POST)
        if choiceformset.is_valid():
            return redirect('survey:make_index', pk)
# >>>>>>> 030893919c333c217b4815b5dd7179e044ea3329
#     field = get_object_or_404(Field, pk=pk)
#     try:
#         selected_choice = field.multiplechoice_set.get(pk=request.POST['multiple_choice'])
#     except (KeyError, MultipleChoice.DoesNotExist):
#         return render(request, 'survey/make_field_mul.html', {'field': field,
#                                                                'error_message':
#                                                                "You didn't select a choice", })
#     else:
#         selected_choice += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('survey:results', args=field.id,))


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
# =======
# def multiple_choice(request, pk):
#     if request.method == "POST":
#         choiceformset = ChoiceFormSet(request.POST)
#         if choiceformset.is_valid():
#             return redirect('survey:make_index', pk)
#     else:
#         data = {
#             'form-TOTAL_FORMS': '1',
#             'form-INITIAL_FORMS': '1',
#             'form-MAX_NUM_FORMS': '10',
#         }
#         choiceformset = ChoiceFormSet(data)
#     return render(request, 'survey/choice.html', {
#         'survey': Survey.objects.get(pk=pk),
#         'choiceformset': choiceformset,
#     })
# >>>>>>> 030893919c333c217b4815b5dd7179e044ea3329


def results(request, pk):
    field = get_object_or_404(Field, pk=pk)
    return render(request, 'survey/results.html', {'field': field})


@login_required()
def my_survey(request):
    user = request.user
    surveys = Survey.objects.filter(author=user)
    return render(request, 'survey/my_survey.html', {
        'surveys': surveys,
    })


@login_required()
def my_survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    if survey.author == request.user:
        return render(request, 'survey/my_survey_detail.html', {
            'survey': survey,
        })
    else:
        return redirect('root')     # TODO: 일단 root 로 이동


@login_required()
def my_survey_complete(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    if survey.author == request.user:
        survey.status = 'c'
        survey.save()
        return render(request, 'survey/my_survey_complete.html', {
            'survey': survey,
        })
    else:
        return redirect('root')     # TODO: 일단 root 로 이동

