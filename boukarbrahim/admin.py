from django.contrib import admin
from .models import Patient,Medecin,Rendezvous,Consultation

# Register your models here.

admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Rendezvous)
admin.site.register(Consultation)

