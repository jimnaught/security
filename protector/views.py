from django.shortcuts import render, redirect
from .forms import ClientsMessagesForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ClientsMessagesForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('protector:index')
    else:
        form = ClientsMessagesForm()
    return render(request, 'index.html',{'form':form})


def contact(request):
    if request.method == 'POST':
        form = ClientsMessagesForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('protector:index')
    else:
        form = ClientsMessagesForm()
    return render(request, 'contact.html',{'form':form})


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')
