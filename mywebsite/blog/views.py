from django.shortcuts import render
from  django.http import HttpResponse

# function to render homepage template
def home(request):
    return render(request, 'blog/home.html')
# function to render about template
def about(request):
    return render(request, 'blog/about.html')