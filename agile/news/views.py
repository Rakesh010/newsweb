from django.shortcuts import render


def home(request):
     return render(request,'INDEX.html')
def ABOUT(request):
     return render(request,'ABOUT.html')
def CONTACT(request):
     return render(request,'CONTACT.html')