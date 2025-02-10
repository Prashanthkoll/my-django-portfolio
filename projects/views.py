from django.shortcuts import render

# Create your views here.
def proj(request):
    return render(request,'proj.html')

def Shadi(request):
    return render(request,'shadi.html')

def netf(request):
    return render(request,'netf.html')