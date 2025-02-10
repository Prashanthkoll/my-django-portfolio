from django.shortcuts import render

# Create your views here.
from skills.models import Skills
def skill(request):
    return render(request,'skill.html')

def read(request,id):
    data=Skills.objects.get(id=id)
    p=data.point.split('@')
    return render(request,'read.html',{'record':data,'re':p})