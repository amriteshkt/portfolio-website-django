from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homepage_new.html')

def thank_you(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Hi! {name}, thank you for contacting me!")
    return render(request, 'thank_you.html')