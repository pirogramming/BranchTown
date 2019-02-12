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
    form = get_object_or_404(Survey, pk=pk)
    field = Survey.objects.get(pk=pk).field_set.all()
    return render(request, 'board/survey_detail.html', {
        'form': form,
        'field_set': field
    })


def survey_interest(request):
    if request.user.is_authenticated:
        tags = request.user.profile.tag.all()
        surveys = Survey.objects.filter(tag__in=tags).distinct()
        print(surveys)
    else:
        surveys = Survey.objects.none()

    return render(request, 'board/survey_interest.html', {
        'surveys': surveys,
    })


def survey_tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    surveys = tag.survey_set.all()
    return render(request, 'board/survey_tag.html', {
        'tag': tag,
        'surveys': surveys,
    })


def survey_hot(request):
    pass


def survey_ongoing(request):
    pass


def survey_answer(request):
    pass


def survey_finish(request):
    pass


def survey_recent(request):
    surveys = Survey.objects.
