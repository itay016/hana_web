from django.db import models

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='therapists/')

    def __str__(self):
        return self.name
    
class header_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='header_section/',blank=True , null=True)
    sec_image = models.ImageField(upload_to='header_section/',blank=True , null=True)

class welcome_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='welcome_section_2/', blank=True, null=True)


class Specialization_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='Specialization_section/', blank=True, null=True)
    
class belive_and_path_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='belives/', blank=True, null=True)

class About_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='About_section/', blank=True, null=True)
    
class certificates_sectoin(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    
class extra_traines(models.Model):
    tittle = models.CharField(max_length=500)
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    image = models.ImageField(upload_to='extra_traines/', blank=True, null=True)
    
class workshopes(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sub_title= models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='workshopes/',blank=True, null=True)
    button_text = models.CharField(max_length=200,blank=True, null=True)
    button_link = models.CharField(max_length=500,blank=True, null=True)
    
class contact_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contant_section/',blank=True, null=True)
    name = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=200,blank=True, null=True)
    button_link = models.CharField(max_length=500,blank=True, null=True)
    
class contact_info(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    address_image = models.ImageField(upload_to='contact_info/', blank=True, null=True)
    phone = models.CharField(max_length=200)
    phone_image = models.ImageField(upload_to='contact_info/', blank=True, null=True)
    email = models.CharField(max_length=200)
    email_image = models.ImageField(upload_to='contact_info/',blank=True, null=True)
    
class fotter_section(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

class upper_navvbar(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    logo = models.ImageField(upload_to='upper_navvbar/',blank=True, null=True)
    related_menue = models.ForeignKey('menue_in', on_delete=models.CASCADE, blank=True, null=True)
    
    
class menue_in(models.Model):
    related_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    related_fileds = models.ManyToManyField('menue_items',blank=True)
    
class menue_items(models.Model):   
    title = models.CharField(max_length=200,blank=True, null=True)
    link = models.CharField(max_length=500,blank=True, null=True)
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.phone}"
