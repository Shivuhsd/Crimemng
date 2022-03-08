from django.contrib.auth.models import User
from django.db import models



# Create your models here.
# This is a Complaint model for user who loged in to lodge a complaint

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    pincode = models.CharField(max_length=6, null=True)
    place = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    subject = models.TextField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    photo = models.ImageField(blank=True, upload_to="complaintphoto/")
    file = models.FileField(blank=True, upload_to="complaintfile/")

    agree = models.BooleanField(null=True)

    def __str__(self):
        return self.firstname + ' | ' +str(self.user)

# This model extends the existing UserModel

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to = "images/profile")
    phone = models.CharField(blank=True, max_length=10)
    address = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return str(self.user)

#This model is for Feedback
class Feedback(models.Model):
    
    submit = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.TextField(max_length=1, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)


#This model is for Contact Us Form
class Contact(models.Model):
    submit = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    message= models.TextField(null=True)

    def __str__(self):
        return str(self.name)

#This is a Criminal Form Only Acceble by a admin or Staff Member

class Profile(models.Model):
    
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    firstname = models.CharField(max_length=200, null= True)
    lastname = models.CharField(max_length=200, null= True)
    image = models.ImageField(upload_to = "images/",null=True)
    phone = models.CharField(max_length=10, null= True)
    place = models.CharField(max_length=50, null=True)
    pincode = models.CharField(max_length=6, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null = True)
    accuser_firstname = models.CharField(max_length=200, null=True)
    accuser_lastname = models.CharField(max_length=200, null=True)
    image_accuser = models.ImageField(upload_to = "images/",null=True)
    accuser_email = models.EmailField(null=True)
    accuser_phone = models.CharField(null=True, max_length=10)
    accuser_pincode = models.CharField(null=True, max_length=6)
    accuser_address = models.TextField(null=True)
    description = models.TextField(null=True)
    fir = models.FileField(upload_to="fir/", null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_edit = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.firstname

class Reply(models.Model):
    replied_on = models.DateTimeField(auto_now_add=True, null=True)
    to = models.ForeignKey(Contact, null=True, on_delete=models.CASCADE)
    message = models.TextField(null=True)

class Evidencei(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    evidence_img = models.ImageField(upload_to='evidence/img', blank=True)

class Evidencea(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    evidence_audio = models.FileField(upload_to='evidence/audio', blank=True)

class Evidencev(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    evidence_video = models.FileField(upload_to='evidence/video', blank=True)

class Evidenced(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    evidence_doc = models.FileField(upload_to='evidence/doc', blank=True)

class Developer(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)