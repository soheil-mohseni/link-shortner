from django.shortcuts import render
from django.http import HttpResponse
from .models import mysaia
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def creaturl(request):
    return render(request, 'saia/myurl.html',{})
    
def send(request):
    return render(request, 'saia/myurl.html',{})
    
    
def do(request):
    port1=request.POST.getlist("portal1")[0]
    port2=request.POST.getlist("portal2")[0]
    external = mysaia()
    external.port1 = port1
    external.port2 = port2
    external.save()
    contex = {
           'portal' : external,  
    
    }
    return render(request, 'saia/done.html',contex)
    
    

def short(request, short):
    url = get_object_or_404(mysaia, port2=short)
    print(url.port1)
    return redirect(url.port1)
