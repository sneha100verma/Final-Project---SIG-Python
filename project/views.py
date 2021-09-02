from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return render(request, 'test.html')


def f1(request):
    return render(request, 'pro1.html')

def f2(request):
    return render(request, 'pro2.html')

def f3(request):
    return render(request, 'pro3.html')
