from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def echo(request):
    response = ''
    if request.method == 'GET':
        if request.GET:
            response += 'get '
            for each in request.GET:
                response += f'{each}: {request.GET[each]} '

    if request.method == 'POST':
        if request.POST:
            response += 'post '
            for each in request.POST:
                response += f'{each}: {request.POST[each]} '

    try:
        response += f'statement is {request.META["HTTP_X-PRINT-STATEMENT"]}'
    except KeyError:
        response += 'statement is empty'
    return HttpResponse(content=response, status=200)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
