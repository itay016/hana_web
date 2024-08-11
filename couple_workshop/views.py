from django.shortcuts import render
from .models import *
from homepage.models import contact_section,contact_info
# Create your views here.

def couples_work_shop(request):
    current_thrapist = Therapist.objects.filter(name = 'בוריה יאיר חנה​').first()
    nav_bar = upper_navvbar.objects.filter(related_therapist =current_thrapist ).first()
    web_details_ = web_details.objects.filter(related_therapist =current_thrapist ).first()
    header_in_ = header_in.objects.filter(related_therapist =current_thrapist ).first()
    contact = contact_section.objects.filter(related_therapist =current_thrapist).first()    
    contact_info_isntance = contact_info.objects.filter(related_therapist =current_thrapist).first()
    page_sections = page_section.objects.filter(related_therapist =current_thrapist)
    out = {
        'tittle':"איך שומרים על האהבה הזו",
        'nav_bar':nav_bar,
        'therapist':current_thrapist, 
        "web_details_":web_details_,
        "header_in_":header_in_,
        "contact":contact,
        "contact_info_isntance":contact_info_isntance,
        "page_sections":page_sections,
    }
    return render(request, 'couplw_work_shop.html',out)