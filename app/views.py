from django.shortcuts import render

# Create your views here.
def siva(request):
    d={'name':'nagesh','age':21}
    return render(request,'siva.html',context=d)


def nagesh(request):
    s={'name':'namgesh','age':23}
    return render(request,'nagesh.html',s)