from django.shortcuts import render
from .models import Reason
import random

def home(request):
    return render(request, 'home.html')

def reasons(request):
    reason = random.choice(Reason.objects.all())
    return render(request, 'reasons.html', {'reason': reason})

def password_page(request):
    if request.method == "POST":
        if request.POST.get("pass") == "dhinglu":
            return render(request, 'letter.html')
    return render(request, 'password.html')

def final(request):
    return render(request, 'final.html')

def onepiece(request):
    return render(request,'onepiece.html')
