from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/index_1.html',)

def aboutUs(request):
    return render(request,'pages/about.html',)

def services(request):
    return render(request,'pages/services.html',)

def contact(request):
    return render(request,'pages/contact.html',)