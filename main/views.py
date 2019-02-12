from django.shortcuts import render


def mainpage(request):
    return render(request, 'main/mainpage.html', {
        'range': range(8),
    })
