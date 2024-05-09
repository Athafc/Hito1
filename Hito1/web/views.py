from django.shortcuts import render, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm
# Create your views here.

def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html')

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {
        'private_flans' :private_flans
    }
    return render(request, 'welcome.html', context)

def contacto(request):
   # public_flans = Flan.objects.filter(is_private=False)
    print(request.POST)
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        #si entro por el metodo get
        #form = ContactFormForm()
        form = ContactFormModelForm()

    context = {'form':form}
    return render(request, 'contact.html', context)

def exito(request):
    return render(request, 'exito.html')