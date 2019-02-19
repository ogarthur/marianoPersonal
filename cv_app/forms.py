from django import forms
from django.core import validators




class FormEmail(forms.Form):

    nombre      = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':' form-control name-form ','placeholder':'Nombre' , 'data-validation-required-message':'Por favor introduzca su nombre.'}),required=True)
    email       = forms.EmailField(label='Email',max_length=300,widget=forms.EmailInput(attrs={ 'class':' form-control','type':'email' ,'placeholder':'Email','required':'required', 'data-validation-required-message':'Por favor introduzca su email.'}),required=True)
    mensaje     = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class':' form-control','rows':'6','placeholder':'Mensaje' ,'data-validation-required-message':'Por favor introduzca su mensaje.'}),required=True)

    def clean(self):
        all_clean_data = super(FormEmail,self).clean()
        nombre  = all_clean_data['nombre']
        email   = all_clean_data['email']
        mensaje = all_clean_data['mensaje']
