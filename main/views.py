from django.shortcuts import render, redirect
from survey.models import Survey
from tag.models import Tag


def mainpage(request):
    survey_recent = Survey.objects.all().order_by('-id')
    if request.user.is_authenticated:
        tags = request.user.profile.tag.all()
        survey_interest = Survey.objects.filter(tag__in=tags).distinct()
    else:
        survey_interest = Survey.objects.all().order_by('-id')  # TODO 일단 board.survey_recent.surveys 와 똑같이 설정 추후 변경해야함

    searched_tag = request.GET.get('tag')
    if Tag.objects.filter(name=searched_tag):
        tag = Tag.objects.get(name=searched_tag)
        return redirect('board:survey_tag', tag.pk)

    return render(request, 'main/mainpage.html', {
        'survey_interest': survey_interest,
        'survey_recent': survey_recent,
    })


def intropage(request):
    return render(request, 'main/introduction.html')


def cspage(request):
    return render(request, 'main/cspage.html')
