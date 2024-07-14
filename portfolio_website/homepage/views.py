from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def projects(request):
    return render(request, 'projects.html')

def contact_me(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
        # print(f"Hi! {name}, thank you for contacting me!")
    return render(request, 'contactme.html')