from django.shortcuts import render, HttpResponse

def home(request):
    return render(HttpResponse, 'hi there')


