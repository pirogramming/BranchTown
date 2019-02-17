from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
from survey.models import Survey, Field, MultipleChoice

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        survey = Survey.objects.get(pk=1)
        field = Field.objects.filter(survey=survey)
        return render(request, 'response/charts.html', {
            "fields": field,
        })


def get_data(request, *args, **kwargs):
    data = {
        'sales': 100,
        'customer': 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        fields = Survey.objects.get(pk=1).field_set.all()

        labels = []
        default_items = []

        choices = fields[0].multiplechoice_set.all()
        choices_len = choices.count()

        for choice in choices:
            labels.append(choice.choice_text)
            default_items.append(choice.votes)


        data = {
            "labels": labels,
            "default": default_items,
        }

        return Response(data)
