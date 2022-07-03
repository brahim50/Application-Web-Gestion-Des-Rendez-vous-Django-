from django.urls import path
from . import views
urlpatterns = [
    path('index.html',views.index,name='index'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('patient.html',views.patient,name='patient'),
    path('delete_patient/<int:myid>/',views.delete_patient,name='delete_patient'),
    path('editpatient/<int:myid>/',views.edit_patient,name='edit_patient'),
    path('update_patient/<int:myid>/',views.update_patient,name='update_patient'),
    path('doctor.html', views.doctor, name='doctor'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('delete_doctor/<int:myid>/',views.delete_doctor,name='delete_doctor'),
    path('rendezvous.html', views.rendezvous, name='rendezvous'),
    path('add_rendezvous', views.add_rendezvous, name='add_rendezvous'),
    path('delete_doctor/<int:myid>/', views.delete_doctor, name='delete_doctor'),

    path('consultation.html', views.consultation, name='consultation'),

    path('add_consultation',views.add_consultation,name='add_consultation'),

    path('delete_consultation/<int:myid>/', views.delete_consultation, name='delete_consultation'),



]