from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioContacto


# Create your views here.


def index(request):
    
        return render(request, 'index.html')

    


def nosotros(request):
    return render(request, 'nosotros.html', {})

def contact_success(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_phone = request.POST['message-phone']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #enviar email

        send_mail(
            'Contacto ItHelper: ' + message_name, #asunto
            message + '. \n \n Teléfono de contacto: ' + message_phone + '. \n Correo: '+ message_email, #mensaje 
            message_email, #emisor
            ['contacto@ithelper.cl'], #receptor

        )

        return render(request, 'contact_success.html', {'message_name': message_name})
    else:
        return render(request, 'contact_success.html', {})


def servicios(request):
    return render(request, 'servicios.html', {})


def certif(request):
    
    return render(request, 'certif.html', {})

    
def store(request):
    return render(request, 'store.html', {})
