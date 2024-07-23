from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def up(request):
    return JsonResponse({"status": "up"})

def index(request):
    return render(request, 'base/pages/index.html')