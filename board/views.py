from django.shortcuts import render, get_object_or_404
from survey.models import Survey, Field


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
