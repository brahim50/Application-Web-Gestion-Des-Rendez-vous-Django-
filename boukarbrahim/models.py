from django.db import models

class Patient(models.Model):
    id = models.IntegerField
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    dateN = models.DateField()

class Medecin(models.Model):
    id = models.IntegerField
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    specialite = models.CharField(max_length=30)

class Rendezvous(models.Model):
        id = models.IntegerField
        date = models.DateField()
        rendezvous = models.CharField(max_length=30)
        nompatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        nomdoctor = models.ForeignKey(Medecin, on_delete=models.CASCADE)
class Consultation(models.Model):
        id = models.IntegerField
        description = models.CharField(max_length=30)
        traitement = models.CharField(max_length=30)
        type = models.CharField(max_length=30)
        idrendezvous = models.ForeignKey(Rendezvous, on_delete=models.CASCADE)






