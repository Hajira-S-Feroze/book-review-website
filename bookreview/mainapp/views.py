from django.shortcuts import render

# Create your views here.
def username(request):
    
    context = {"username":"hajira"}
    return render(request, "mainapp/userlogin.html", context)