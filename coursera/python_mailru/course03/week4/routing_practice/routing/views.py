from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(content={}, status=200)
    else:
        return HttpResponse(status=405)


def slug_route(request, pk):
    if request.method == 'GET':
        return HttpResponse(content=pk, status=200)


def sum_route(request, a, b):
    if request.method == 'GET':
        content = int(a) + int(b)
        return HttpResponse(content=content, status=200)


def sum_get_method(request):
    if request.method == 'GET':
        try:
            a = request.GET['a']
            b = request.GET['b']
        except MultiValueDictKeyError:
            return HttpResponse(status=400)

        try:
            content = int(a) + int(b)
            return HttpResponse(content=content, status=200)
        except ValueError:
            return HttpResponse(status=400)


def sum_post_method(request):
    if request.method == 'POST':
        try:
            a = request.POST['a']
            b = request.POST['b']
        except MultiValueDictKeyError:
            return HttpResponse(status=400)

        try:
            content = int(a) + int(b)
            return HttpResponse(content=content, status=200)
        except ValueError:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)
