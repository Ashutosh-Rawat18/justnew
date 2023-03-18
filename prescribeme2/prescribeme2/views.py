from django.shortcuts import render
from django.contrib import messages
from prescribeme2.models import DocModel
from prescribeme2.models import Premodel
from prescribeme2.forms import Preforms

# Create your views here.


def docreg(request):
    if request.method == "POST":
        if request.POST.get('docname') and request.POST.get('age') and request.POST.get('email') and request.POST.get('phoneno') and request.POST.get('address') and request.POST.get('licenseno') and request.POST.get('password'):
            saverecord = DocModel()
            saverecord.docname = request.POST.get('docname')
            saverecord.age = request.POST.get('age')
            saverecord.email = request.POST.get('email')
            saverecord.phoneno = request.POST.get('phoneno')
            saverecord.address = request.POST.get('address')
            saverecord.licenseno = request.POST.get('licenseno')
            saverecord.password = request.POST.get('password')
            saverecord.save()
            messages.success(request, 'Account ' +
                             saverecord.docname + ' is created successfully')
            return render(request, 'doctor_signup.html')
    else:
        return render(request, 'doctor_signup.html')


# def dashboard(request):
#     return render(request, 'Dashboard.html')

def showpre(request):
    showall = Premodel.objects.all()
    return render(request, 'Dashboard.html', {"data": showall})


def insertpre(request):
    if request.method == "POST":
        if request.POST.get('docname') and request.POST.get('symptom') and request.POST.get('dates') and request.POST.get('medicine1') and request.POST.get('when1') and request.POST.get('medicine2') and request.POST.get('when2'):
            saverec = Premodel()
            saverec.id = request.POST.get('id')
            saverec.docname = request.POST.get('docname')
            saverec.symptom = request.POST.get('symptom')
            saverec.dates = request.POST.get('dates')
            saverec.medicine1 = request.POST.get('medicine1')
            saverec.when1 = request.POST.get('when1')
            saverec.medicine2 = request.POST.get('medicine2')
            saverec.when2 = request.POST.get('when2')
            saverec.save()
            messages.success(request, 'Prescription saved successfully')
            return render(request, 'pescription.html')
    else:
        return render(request, 'pescription.html')


def editpre(request, id):
    editpreobj = Premodel.objects.get(id=id)
    return render(request, 'edit.html', {"Premodel": editpreobj})


def updatepre(request, id):
    Updatepre = Premodel.objects.get(id=id)
    form = Preforms(request.POST, instance=Updatepre)
    if form.is_valid():
        form.save()
        messages.success(request, 'Prescription updated successfully')
        return render(request, 'edit.html', {"Premodel": Updatepre})


def delpre(request, id):
    deletepre = Premodel.objects.get(id=id)
    deletepre.delete()
    showdata = Premodel.objects.all()
    return render(request, 'Dashboard.html', {"data": showdata})
