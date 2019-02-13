from django.shortcuts import render
from survey.models import Survey


def mainpage(request):
    if request.user.is_authenticated:
        tags = request.user.profile.tag.all()
        surveys = Survey.objects.filter(tag__in=tags).distinct()
    else:
        surveys = Survey.objects.all().order_by('-id')  # TODO 일단 board.survey_recent.surveys 와 똑같이 설정 추후 변경해야함

    return render(request, 'main/mainpage.html', {
        'surveys': surveys,
        'range': range(8),
    })
