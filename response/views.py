import json

from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.views.generic import View
from django.contrib.auth import get_user_model

from response.forms import TextAnswerForm
from response.models import Response
from survey.models import Survey, Field, MultipleChoice, TextAnswer

User = get_user_model()


class HomeView(View):
    def get(self, request, pk=1):

        fields = Field.objects.filter(
            survey__id=pk, type=1
        )

        data = {}
        for field in fields:
            data[field.id] = {'question': field.question, 'labels': [], 'votes': []}
            for choice in field.multiplechoice_set.all():
                data[field.id]['labels'].append(choice.choice_text)
                data[field.id]['votes'].append(choice.votes)
        print(data)

        return render(request, 'response/charts.html',
                      context={
                          'json_graphs': mark_safe(json.dumps(data)),
                          'graphs': data
                      })


def preview_survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'response/preview.html', {
        'survey': survey,
    })


def response_survey(request, pk):
    survey = Survey.objects.get(pk=pk)
    fields = survey.field_set.all()
    if request.method == 'POST':
        for field in fields:
            if field.type == '2':
                if request.POST.get('%d' % field.id):
                    answer = TextAnswer.objects.create(field=field, answer=request.POST.get('%d' % field.id))
            elif field.type == '1':
                if request.POST.get('%d' % field.id):
                    choice = MultipleChoice.objects.get(pk=request.POST.get('%d' % field.id))
                    choice.votes += 1
                    choice.save()
        return redirect('response:join_survey', pk)
    return render(request, 'response/survey.html', {
        'survey': survey,
        'fields': fields,
    })


# def response_survey_text(request, pk):
#     fields = Survey.objects.get(pk=pk).field_set.all()
#     text_answer_formset = formset_factory(form=TextAnswerForm, max_num=fields.count())
#     if request.method == 'POST':
#         formset = text_answer_formset(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 answer = form.save()
#             return redirect('root')
#     else:
#         # initial = []
#         # for field in fields:
#         #     initial.append({'field': field})
#         #     print(field)
#         # formset = text_answer_formset(initial=initial)
#         formset = text_answer_formset(initial=[{
#             'field': field,
#         } for field in fields])
#     return render(request, 'response/practice_text.html', {
#         'fields': fields,
#         'formset': formset,
#     })
#
def join_survey(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user.is_authenticated:
        respondent = Response.objects.create(respondent=request.user, survey=survey)
    survey.response_count += 1
    survey.save()
    return redirect('root') # TODO: redirect 수정
g