from django.shortcuts import render
from django.http import JsonResponse
import re

# Create your views here.
def index(request):
    return render(request, 'foods/pages/index.html')
