from django.http import HttpResponse
feom django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')


def about(request):
    return render(request, 'home.html',{'greeting':'Hello!'})
