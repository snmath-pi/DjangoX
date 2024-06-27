from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_discription = data.get('receipe_discription')
        receipe_image = request.FILES['receipe_image']
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_discription = receipe_discription,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
        
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    
    if request.method== "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_discription = data.get('receipe_discription')
        receipe_image = request.FILES.get('receipe_image')
        queryset.receipe_name = receipe_name
        queryset.receipe_discription = receipe_discription
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')
    
    context = {'receipe': queryset}
    return render(request, 'update_receipes.html', context)
    