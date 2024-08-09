from django.shortcuts import render,redirect
from .models import *

def homepage(request):
    current_thrapist = Therapist.objects.filter(name = 'בוריה יאיר חנה​').first()
    nav_bar = upper_navvbar.objects.filter(related_therapist =current_thrapist ).first()
    out = {
        "nav_bar":nav_bar
    }
    return render(request,'homepage.html',out)