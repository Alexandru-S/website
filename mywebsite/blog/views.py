from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'author': 'AlexMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '2020-03-30'
    },
    {
        'author': 'RazvanMS',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '2020-03-31'
    }


]
# function to render homepage template
def home(request):
    context = {'posts':posts,'title':'Home'}
    return render(request, 'blog/home.html', context)


# function to render about template
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})