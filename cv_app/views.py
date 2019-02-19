from django.shortcuts import render
from cv_app import user_information
from . import forms
from cv_app.forms import FormEmail
# Create your views here.

def index(request):
    print("Recargando")
    consulta_form = forms.FormEmail()
    data = user_information.test_user_data

    if request.method == 'POST':
        consulta_form = forms.FormEmail(request.POST)

        if consulta_form.is_valid():
            dataset={
                    'nombre':str(consulta_form.cleaned_data['nombre']),
                    'email':str(consulta_form.cleaned_data['email']),
                    'mensaje':str(consulta_form.cleaned_data['mensaje']),
            }
            print("RECIBIDO")
            print(dataset)
            return render(request,'cv_app/cv.html',{'consulta':consulta_form,'user_data':data})
        else:

            return render(request,'cv_app/cv.html',{'consulta':consulta_form,'user_data':data})
    else:
        return render(request,'cv_app/cv.html',{'consulta':consulta_form,'user_data':data})
