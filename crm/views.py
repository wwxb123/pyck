from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
app_name = 'projects'
def index(request):
    return HttpResponse("crm应用视图")