from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Patient,Medecin,Rendezvous,Consultation
from .filters import PatientFilter
from django.core.paginator import Paginator
from .forms import LoginForm
from django.contrib.auth import authenticate ,login

def index(request):
    return render(request, 'pages/index.html')


def patient(request):
    context = {}
    filtered_patient = PatientFilter(
        request.GET,
        queryset=Patient.objects.all()
    )

    context['filtered_patient'] = filtered_patient

    paginated_filtered_patient = Paginator(filtered_patient.qs, 3)
    page_number = request.GET.get('page')
    patient_page_obj = paginated_filtered_patient.get_page(page_number)

    context ['patient_page_obj'] = patient_page_obj

    return render(request, 'pages/patient.html',context=context)

def doctor(request):
    medecins = Medecin.objects.all()
    context = {
        'medecins': medecins,

    }
    return render(request, 'pages/doctor.html',context)

def rendezvous(request):
    patients = Patient.objects.all()
    medecins = Medecin.objects.all()
    rendez = Rendezvous.objects.all()
    context = {
        'patients': patients,
        'medecins': medecins,
        'rendez': rendez,

    }
    return render(request, 'pages/rendezvous.html',context)

def consultation(request):
    rendez = Rendezvous.objects.all()
    consultation = Consultation.objects.all()

    context = {
        'rendez': rendez,
        'consultation': consultation,

    }

    return render(request, 'pages/consultation.html',context)



def add_patient(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        dateN = request.POST['dateN']
        patients= Patient(nom=nom, prenom=prenom, email=email, dateN=dateN)
        patients.save()
        patients = Patient.objects.all()
        context = {
            'patients': patients,

        }
    else:
        pass
    return render(request, 'pages/patient.html',context)
def delete_patient(request,myid):
    patients = Patient.objects.get(id = myid)
    patients.delete()
    return redirect(patient)

def edit_patient(request,myid):
    patients = Patient.objects.get(id=myid)
    sel_patient = Patient.objects.all()
    context = {
        'patients': patients,
        'sel_patient':  sel_patient,
    }
    return render(request, 'pages/editpatient.html',context)


def update_patient(request,myid):
    patients = Patient.objects.get(id=myid)
    patients.nom = request.POST['nom']
    patients.prenom = request.POST['prenom']
    patients.email = request.POST['email']
    patients.dateN = request.POST['dateN']
    patients.save()
    return redirect(patient)



def add_doctor(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        specialite = request.POST['specialite']
        medecins= Medecin(nom=nom, prenom=prenom, specialite=specialite)
        medecins.save()
        medecins = Medecin.objects.all()
        context = {
            'medecins': medecins,

        }
    else:
        pass
    return render(request, 'pages/doctor.html',context)

def delete_doctor(request,myid):
    medecins = Medecin.objects.get(id = myid)
    medecins.delete()
    return redirect(doctor)



def add_rendezvous(request):
    if request.method == "POST":
        date = request.POST['date']
        rendezvous = request.POST['rendezvous']
        nompatient_id = request.POST['nompatient_id']
        nomdoctor_id = request.POST['nomdoctor_id']
        rendez= Rendezvous(date=date, rendezvous=rendezvous, nompatient_id=nompatient_id, nomdoctor_id=nomdoctor_id)
        rendez.save()
        rendez = Rendezvous.objects.all()
        patients = Patient.objects.all()
        medecins = Medecin.objects.all()
        context = {
            'rendez': rendez,
            'patients': patients,
            'medecins': medecins,

        }
    else:
        pass
    return render(request, 'pages/rendezvous.html',context)


def delete_doctor(request,myid):
    rendez = Rendezvous.objects.get(id = myid)
    rendez.delete()
    return redirect(rendezvous)






def add_consultation(request):
    if request.method == "POST":
        description = request.POST['description']
        traitement = request.POST['traitement']
        type = request.POST['type']
        idrendezvous_id = request.POST['idrendezvous_id']
        consultation= Consultation(description=description, traitement=traitement, type=type, idrendezvous_id=idrendezvous_id)
        consultation.save()
        consultation = Consultation.objects.all()
        rendez = Rendezvous.objects.all()
        context = {
            'consultation': consultation,
            'rendez': rendez,

        }
    else:
        pass
    return render(request, 'pages/consultation.html',context)



def delete_consultation(request,myid):
    consultation = Consultation.objects.get(id = myid)
    consultation.delete()
    return redirect(consultation)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request)
