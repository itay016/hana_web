from django.db import models
from homepage.models import Therapist
# Create your models here.
class menue_in(models.Model):
    related_therapist = models.ForeignKey(Therapist,related_name="meue_workshop", on_delete=models.CASCADE)
    related_fileds = models.ManyToManyField('menue_items',blank=True)
    menue_name = models.CharField(max_length=200, blank=True, null=True)
    
class web_details(models.Model):
    related_therapist = models.ForeignKey(Therapist, related_name="web_details", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='web_details/', blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    apear_num = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    
    
    
class menue_items(models.Model):   
    title = models.CharField(max_length=200,blank=True, null=True)
    link = models.CharField(max_length=500,blank=True, null=True)
    
class upper_navvbar(models.Model):
    related_therapist = models.ForeignKey(Therapist,related_name="nav", on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    logo = models.ImageField(upload_to='upper_navvbar/',blank=True, null=True)
    related_menue = models.ForeignKey('menue_in', on_delete=models.CASCADE, blank=True, null=True)

class header_in(models.Model):
    related_therapist = models.ForeignKey(Therapist,related_name="head", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='header_in/', blank=True, null=True)

class page_section(models.Model):
    related_therapist = models.ForeignKey(Therapist,related_name="pagesec", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    sub_tittle = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='page_section/', blank=True, null=True)
    page_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    apear_num = models.IntegerField(default=0)