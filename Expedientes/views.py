from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Expedientes.models import registroExpediente
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def gestionExpedientes(request):
    listadoExpediente = registroExpediente.objects.all().order_by("-fechaApertura")[:5]
    return render(request, "gestionExpedientes.html", {"expedientes": listadoExpediente})

@login_required
def registrarExtranjero(request):
    numNue = request.POST['txtnumNue']
    numNut = request.POST['txtnumNut']
    numExpediente = request.POST['txtnumExpediente']
    fechaApertura = request.POST['txtfechaApertura']
    nombre = request.POST['txtnombre']
    nacionalidad = request.POST['txtnacionalidad']
    fechaNacimiento = request.POST['txtfechaNacimiento']

    registroExpediente.objects.filter(numNue=numNue)
    registroExistente = registroExpediente.objects.filter(numNue=numNue)
    if registroExistente.exists():
        return redirect('/')

    registrar = registroExpediente.objects.create(
        numNue=numNue, numNut=numNut, numExpediente=numExpediente, fechaApertura=fechaApertura,
        nombre=nombre, nacionalidad=nacionalidad, fechaNacimiento=fechaNacimiento)
    return redirect('/')

@login_required
def eliminarExpediente(request, numNue):
    expediente = registroExpediente.objects.get(numNue=numNue)
    expediente.delete()

    return redirect('listaexp')

@login_required
def listadoExpedientes(request, ):
    numNue = request.GET.get("numNue", None)
    if (numNue):
        lista = registroExpediente.objects.filter(numNue=numNue).order_by("fechaApertura")
    else:
        lista = registroExpediente.objects.all().order_by("fechaApertura")
    return render(request, "listaExpedientes.html", {"lista": lista})

@login_required
def edicionExpedientes(request, numNue):
    expediente = registroExpediente.objects.get(numNue=numNue)
    return render(request, "edicionExpedientes.html", {"expediente": expediente})

@login_required
def editarExpediente(request):
    numNue = request.POST['txtnumNue']
    numNut = request.POST['txtnumNut']
    numExpediente = request.POST['txtnumExpediente']
    fechaApertura = request.POST['txtfechaApertura']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    nacionalidad = request.POST['txtnacionalidad']
    fechaNacimiento = request.POST['txtfechaNacimiento']

    expediente = registroExpediente.objects.get(numNue=numNue)
    expediente.numNue = numNue
    expediente.numNut = numNut
    expediente.numExpediente = numExpediente
    expediente.fechaApertura = fechaApertura
    expediente.nombre = nombre
    expediente.sexo = sexo
    expediente.nacionalidad = nacionalidad
    expediente.fechaNacimiento = fechaNacimiento
    expediente.save()
    return redirect('listaexp')

@login_required
def upload_file(request, numNue):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            expediente = registroExpediente.objects.get(numNue=numNue)
            expediente.expedientePDF=form.files["upload"]
            expediente.save()
            return HttpResponseRedirect('/listadoExpedientes/')
    else:
        form = UploadFileForm()
    return render(request, 'expedientePDF.html', {'form': form})

@login_required
def confirmacionEliminar(request, numNue):
    return render(request, "confirmacionEliminar.html", {"numNue": numNue})