from django.contrib import admin
from . models import Complaint, Contact, Evidencea, Evidenced, Evidencev, Profile, Reply, UserProfile, Evidencei

# Register your models here.

admin.site.register(Complaint)
admin.site.register(Profile)
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(Reply)
admin.site.register(Evidencei)
admin.site.register(Evidencea)
admin.site.register(Evidenced)
admin.site.register(Evidencev)

