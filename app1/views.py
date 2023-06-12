from django.shortcuts import render

# Create your views here.
def formreg(request):
    return render(request,'formreg.html')

def jspiders(request):
    return render(request,'jspiders.html')

def semantictags(request):
    return render(request,'semantictags.html')

def resumetask(request):
    return render(request,'resumetask.html')

def onlinejobform(request):
    return render(request,'onlinejobform.html')

def menubar(request):
    return render(request,'menubar.html')