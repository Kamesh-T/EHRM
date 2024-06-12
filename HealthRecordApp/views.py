from django.shortcuts import render
from .models import HealthRecord
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def Table_view(request):
    Patient_Record = HealthRecord.objects.all()
    return render(request,'HealthRecordApp/Table.html',{
        'data':Patient_Record})

def Home_view(request):
    return render(request,'HealthRecordApp/Home.html',{})