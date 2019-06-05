from django.shortcuts import render, HttpResponse, redirect

def base(request):
    return render(request, 'home.html', {})