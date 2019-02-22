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

class ResultView(View):
    def get(self, request, pk=4):
        survey = Survey.objects.get(pk=pk)


        #전체를 순회할 데이터 set
        fields = Field.objects.filter(
            survey__id=pk
        )

        field_data = {}
        for field in fields:
            field_data[field.id] = {'type': field.type, 'question': field.question}


        #주/단답식 결과 출력
        txt_fields = Field.objects.filter(
            survey__id=pk, type=2|3
        )

        txt_data = {}
        for field in txt_fields:
            txt_data[field.id] = {'question': field.question, 'answer': []}
            for answer in field.textanswer_set.all():
                txt_data[field.id]['answer'].append(answer.answer)


        print(txt_data)

        #객관식 결과 출력
        multi_fields = Field.objects.filter(
            survey__id=pk, type=1
        )

        multi_data = {}
        for field in multi_fields:
            multi_data[field.id] = {'question': field.question, 'labels': [], 'votes': []}
            for choice in field.multiplechoice_set.all():
                multi_data[field.id]['labels'].append(choice.choice_text)
                multi_data[field.id]['votes'].append(choice.votes)


        return render(request, 'response/charts.html',
                      context={
                          'survey': survey,

                          'json_graphs': mark_safe(json.dumps(multi_data)),
                          'graphs': multi_data,

                          'json_txt': mark_safe(json.dumps(txt_data)),
                          'json_fields': mark_safe(json.dumps(field_data)),

                          'txt': txt_data,
                          'fields': field_data,

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
        print(1)
        for field in fields:
            if field.type == '3':
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



def join_survey(request, pk):
    survey = Survey.objects.get(pk=pk)
    if request.user.is_authenticated:
        respondent = Response.objects.create(respondent=request.user, survey=survey)
    survey.response_count += 1
    survey.save()
    return render(request, 'response/join_survey.html', {
        'survey': survey,
    })

