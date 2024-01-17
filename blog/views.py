from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'record.html')

def page2(request):
    return render(request,'record2.html')
# Create your views here.
