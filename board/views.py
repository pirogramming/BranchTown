from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from survey.models import Survey
from tag.models import Tag


def main(request):
    surveys = Survey.objects.all().order_by('-id')
    return render(request, 'board/survey_base.html', {
        'category': 'All Survey',
        'surveys': surveys,
    })


@login_required
def survey_interest(request):
    if request.user.is_authenticated:
        tags = request.user.profile.tag.all()
        surveys = Survey.objects.filter(tag__in=tags).distinct()
    else:
        surveys = Survey.objects.none()

    return render(request, 'board/survey_base.html', {
        'category': 'Recommended',
        'surveys': surveys,
    })


def survey_tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    surveys = tag.survey_set.all()
    return render(request, 'board/survey_base.html', {
        'category': tag.name,
        'surveys': surveys,
    })


def survey_ongoing(request):
    surveys = Survey.objects.filter(status='o')
    return render(request, 'board/survey_base.html', {
        'category': 'Ongoing',
        'surveys': surveys,
    })


@login_required()
def survey_participated(request):
    surveys = Survey.objects.filter(response__respondent_id=request.user)
    return render(request, 'board/survey_base.html', {
        'category': 'Participated',
        'surveys': surveys,
    })


def survey_complete(request):
    surveys = Survey.objects.filter(status='c')
    return render(request, 'board/survey_base.html', {
        'category': 'Completed',
        'surveys': surveys,
    })
