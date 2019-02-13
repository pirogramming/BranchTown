from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'response/charts.html')


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
        qs_count = User.objects.all().count()
        labels = ["1", "2", "3", "4"]
        default_items = [qs_count, 1234, 4455, 5000]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
