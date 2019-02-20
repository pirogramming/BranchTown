from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from survey.models import Survey, Field
from tag.models import Tag


def survey_list(request):
    qs = Survey.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'board/survey_list.html', {
        'form_list': qs,
    })


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    field = survey.field_set.all()
    return render(request, 'board/survey_detail.html', {
        'survey': survey,
        'fields': field,
    })


def main(request):
    surveys = Survey.objects.all()
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
        'category': 'Recommend',
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



def survey_complete(request):
    surveys = Survey.objects.filter(status='c')
    return render(request, 'board/survey_base.html', {
        'category': 'Completed',
        'surveys': surveys,
    })


def survey_recent(request):
    surveys = Survey.objects.all().order_by('-id')  # TODO 너무 많아지면 slicing
    return render(request, 'board/survey_base.html', {
        'category': 'Recent',
        'surveys': surveys,
    })
