from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

from .models import *

# The index
def index(request):

  context = {
    'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
  }
  return render(request, 'index.html', context) 

# Simulate API Call
def hello(request):
    return JsonResponse({'message': 'Hello from Django & DaisyUI!'})
