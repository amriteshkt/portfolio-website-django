from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def projects(request):
    return render(request, 'projects.html')

def contact_me(request):
    return render(request, 'contactme.html')