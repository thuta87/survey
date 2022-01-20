from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Formsurvey
from .models import Survey

def thanks(request):
    #survey= Survey(request.POST or None)

    vdata=Survey()
    vdata.paraid_id=request.POST.get('paraid',0)
    vdata.desc=request.POST.get('desc','')
    vdata.points=request.POST.get('points',0)
    
    if request.POST.get('paraid',0)!=0 and request.POST.get('points',0)!=0:
        vdata.save()
  
    context= {'survey': vdata }
        
    return render(request, 'accounts/thanks.html', context)


    """"
    did=request.POST.get('paraid',0)
    desc=request.POST.get('desc','')
    points=request.POST.get('points',0)

    print(did)
    print(desc)
    print(points)
    survey=Survey(paraid=request.POST&#91;'paraid'], desc=request.POST&#91;'desc'], points=request.POST&#91;'points'])
    survey.save()
    
    if request.POST.get('paraid',''):
        if request.method == 'POST':        
            return render(request,'accounts/thanks.html',)
        else
            return redirect('/')
    else
        return redirect('/')
    """

def home(request):
    #return HttpResponse('Home Page')
    paraid=request.GET["paraid"]
    print(paraid)
    if (paraid):
        return render(request,'accounts/home.html',{'paraid':paraid})

def profile(request):
    #return HttpResponse('Profile Page')
    return render(request,'accounts/profile.html')

def showform(request):
    form= Formsurvey(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'accounts/home.html', context)
    

# Create your views here.
