import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import View
from django.contrib.auth import get_user_model
from survey.models import Survey, Field, MultipleChoice

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

