from django.shortcuts import render

# Create your views here.
def proj(request):
    return render(request,'proj.html')