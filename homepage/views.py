from django.shortcuts import render,redirect
from .models import *


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from couple_workshop.models import web_details

def homepage(request):
    current_thrapist = Therapist.objects.filter(name = 'בוריה יאיר חנה​').first()
    nav_bar = upper_navvbar.objects.filter(related_therapist =current_thrapist ).first()
    hero_section = header_section.objects.filter(related_therapist =current_thrapist ).first()
    welcome_section_in = welcome_section.objects.filter(related_therapist =current_thrapist ).first()
    specilizations = Specialization_section.objects.filter(related_therapist =current_thrapist)
    ibelive = belive_and_path_section.objects.filter(related_therapist =current_thrapist ).first()
    about_me = About_section.objects.filter(related_therapist =current_thrapist ).first()
    certifications = certificates_sectoin.objects.filter(related_therapist =current_thrapist)
    excra_trains = extra_traines.objects.filter(related_therapist =current_thrapist).first()
    workshopes_section = workshopes.objects.filter(related_therapist =current_thrapist).first()
    contact = contact_section.objects.filter(related_therapist =current_thrapist).first()    
    contact_info_isntance = contact_info.objects.filter(related_therapist =current_thrapist).first()
    web_details_ = web_details.objects.filter(related_therapist =current_thrapist ).first()

    out = {
        "web_details_":web_details_,    
        "tittle":"בוריה חנה יאיר פסיכותרפיסטית",
        "current_thrapist":current_thrapist,
        "nav_bar":nav_bar,
        "hero_section":hero_section,
        "welcome_section":welcome_section_in,
        "specilizations":specilizations,
        "ibelive":ibelive,
        "about_me":about_me,
        "certifications":certifications,
        "excra_trains":excra_trains,
        "workshopes_section":workshopes_section,
        "contact":contact,
        "contact_info_isntance":contact_info_isntance,
    }
    return render(request,'homepage.html',out)

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        # שמירת ההודעה במסד הנתונים
        instance = serializer.save()

        # שליחת מייל
        subject = "הודעה חדשה מהאתר"
        message = f"Name: {instance.name}\nPhone: {instance.phone}\nEmail: {instance.email}\n\nMessage:\n{instance.message}"
        send_mail(
            subject,
            message,
            'hana@gmail.com',  # כתובת האימייל שממנה ישלח המייל
            ['ybhana@gmail.com'],  # כתובת האימייל שאליה ישלח המייל
            fail_silently=False,
        )
        return instance
