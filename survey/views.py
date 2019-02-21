from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey, Field

from .forms import SurveyForm, FieldForm, TextAnswerForm, ChoiceFormSet

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





def text_answer(request, pk):
    if request.method == "POST":
        form = TextAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.survey = Survey.objects.get(pk=pk)
            answer.type = '1'
            answer.save()
            return redirect('survey:make_index', pk)
    else:
        form = TextAnswerForm()
    return render(request, 'survey/text_answer.html', {
        'survey': Survey.objects.get(pk=pk),
        'form': form,
    })


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
