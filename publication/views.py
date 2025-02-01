from django.shortcuts import render

# Create your views here.
def pub(request):
    return render(request,'pub.html')