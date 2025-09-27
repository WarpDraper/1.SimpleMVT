from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Hello team!")
def add_Category(request):
    return render(request, 'add_category.html')
def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'categories.html')