from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def up(request):
    return JsonResponse({"status": "up"})


def baseGetIndex(request):
    return render(request, 'base/pages/index.html')


def baseGetAbout(request):
    return render(request, 'base/pages/about.html')
