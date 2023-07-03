
from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm 
import datetime

from .models import (create_nuevo_curso,
                     create_nuevo_card,
                     create_nuevo_publicacion,
                     create_new_consultas,
                     new_class_hospital,
                     new_class_servicio,
                     Usuario)
class form_is_curso(forms.Form):
    curso_activo = forms.CharField(max_length=10)
    btn_pub_curso = forms.CharField(max_length=6, required=False)
    
class estado_curso(forms.Form):
    id_curso_estado = forms.CharField(max_length=10)
    bool_estado_post = forms.CharField(max_length=6)

class delete_user_form(forms.Form):
    usuario_eliminado = forms.CharField(max_length=10)

class form_descarga_postulacion(forms.Form):
    id_buscador =  forms.CharField(max_length=10)

class form_filtro_cursos_nombre(forms.Form):
    nombre_curso_buscar = forms.CharField(max_length=100, required=False)


class form_filtro_cursos_time(forms.Form):
    prox_end_curso_buscar = forms.CharField(max_length=100, required=False)


class form_filtro_cursos_servicio(forms.Form):
    servicio_curso_buscar = forms.CharField(max_length=100, required=False)


class form_filtro_cursos_hospital(forms.Form):
    hospital_curso_buscar = forms.CharField(max_length=100, required=False)


class form_filtro_cursos_personal(forms.Form):
    personal_curso_buscar = forms.CharField(max_length=100, required=False)


class form_busqueda_consulta_respondidas(forms.Form):
    busqueda_consulta_respondidas = forms.CharField(
        max_length=100, required=False)


class form_busqueda_consulta(forms.Form):
    busqueda_consulta = forms.CharField(max_length=100, required=False)


class form_busqueda_curso_operador(forms.Form):
    busqueda_curso_operador = forms.CharField(max_length=100, required=False)


class CreateNewConsultaRespondido(forms.Form):
    id_respuesta = forms.CharField()


class validar_delete_card(forms.Form):
    id_delete_card = forms.CharField()


class validar_delete_cursos(forms.Form):
    id_delete_curso = forms.CharField()


class validar_delete_public(forms.Form):
    id_delete_public = forms.CharField()


class validar_delete_hospital(forms.Form):
    id_delete_hospital = forms.CharField()


class validar_delete_servicio(forms.Form):
    id_delete_servicio = forms.CharField()


class validar_delete_consulta(forms.Form):
    id_delete = forms.CharField()


class validar_curso_publicar(forms.Form):
    id_curso_pub = forms.CharField()

class CreateNewCard(forms.ModelForm):
    
    img_card =  forms.ImageField()
    nombre_card = forms.CharField(max_length=25)
    cargo_card = forms.CharField(max_length=100)
    descrip_card = forms.CharField(max_length=100)

    class Meta:
        model = create_nuevo_card
        exclude = ()
    def clean_img_card(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_card",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            # handle empty image
            raise ValidationError("Por favor sube una imagen")
        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image

    def clean_nombre_card(self):
        nombre = self.cleaned_data.get("nombre_card", False)
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre") 
        validador = str(nombre).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        if len(nombre) >= 26:
            raise ValidationError("Maximo 25 caracteres")
        return nombre

    def clean_cargo_card(self):
        cargo = self.cleaned_data.get("cargo_card")
        if not cargo:
            raise ValidationError("Tiene que ingresar un cargo")
        validador = str(cargo).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        if len(cargo) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return cargo

    def clean_descrip_card(self):
        descrip_card = self.cleaned_data.get("descrip_card")
        if not descrip_card:
            raise ValidationError("Tiene que ingresar un Nombre")
        if len(descrip_card) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return descrip_card


class CreateNewPublication(forms.ModelForm):

    img_pub = forms.ImageField()
    nombre_pub = forms.CharField(max_length=100)
    descrip_pub = forms.CharField(max_length=100)

    class Meta:
        model = create_nuevo_publicacion
        exclude = ()

    def clean_img_pub(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_pub",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            # handle empty image
            raise ValidationError("Por favor sube una imagen")
        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image

    def clean_nombre_pub(self):
        nombre = self.cleaned_data.get("nombre_pub")
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre")
        if len(nombre) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return nombre

    def clean_descrip_pub(self):
        descrip_pub = self.cleaned_data.get("descrip_pub")
        if not descrip_pub:
            raise ValidationError("Por favor ingrese una descripción")
        if len(descrip_pub) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return descrip_pub


class CreateNewCursos(forms.ModelForm):

    nombre_curso = forms.CharField(max_length=70)
    img_curso =  forms.ImageField()
    form_carga_curso = forms.FileField()
    descrip_corta_curso = forms.CharField(max_length=250)
    descrip_larga_curso = forms.CharField(max_length=600)
    requisitos_curso = forms.CharField(max_length=100)
    time_start_curso = forms.DateField() 
    time_end_curso = forms.DateField() 
    servicio_curso = forms.CharField(max_length=100)
    hospital_curso = forms.CharField(max_length=100)
    personal_cursos = forms.CharField(max_length=80)

    class Meta:

        model = create_nuevo_curso
        exclude = ()

    def clean_nombre_curso(self):
        nombre = self.cleaned_data.get("nombre_curso",  False)
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre")
        if len(nombre) >= 71:
            raise ValidationError("Maximo 70 caracteres")
        return nombre

    def clean_img_curso(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_curso",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            raise ValidationError("Por favor sube una imagen")

        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image

    def clean_form_carga_curso(self):
        DOCUMENTS_FILE_TYPES = ['docx', 'xlsx', 'pptx', 'pdf']
        uploaded_document = self.cleaned_data.get("form_carga_curso",  False)
        extension = str(uploaded_document).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_document:
            raise ValidationError("Por favor sube un documento")

        if file_type not in DOCUMENTS_FILE_TYPES:
            raise ValidationError(
                "El archivo tiene que ser un documento de word o PDF.")
        return uploaded_document

    def clean_descrip_corta_curso(self):
        descip_corta = self.cleaned_data.get("descrip_corta_curso",  False)
        if not descip_corta:
            raise ValidationError(
                "Por favor ingrese una descripción para precentar")
        if len(descip_corta) >= 201:
            raise ValidationError("Maximo 200 caracteres")
        return descip_corta

    def clean_descrip_larga_curso(self):
        descip_larga = self.cleaned_data.get("descrip_larga_curso",  False)
        if not descip_larga:
            raise ValidationError("Por favor ingrese una descripción")
        if len(descip_larga) >= 601:
            raise ValidationError("Maximo 600 caracteres")
        return descip_larga

    def clean_requisitos_curso(self):
        requisito = self.cleaned_data.get("requisitos_curso",  False)
        if not requisito:
            raise ValidationError(
                "Por favor ingrese Requisitos para aprobar curso")
        if len(requisito) >= 201:
            raise ValidationError("Maximo 200 caracteres")
        return requisito

    def clean_time_start_curso(self):
        fecha_start = self.cleaned_data.get("time_start_curso")
        hoy = datetime.datetime.now().date()
        if fecha_start is None:
            raise ValidationError("Por favor ingrese una fecha")
        if fecha_start < hoy:
            raise ValidationError("No se pueden ingresar fechas pasadas")
        return fecha_start

    def clean_time_end_curso(self):
        cleaned_data = super().clean()
        fecha_end = self.cleaned_data.get("time_end_curso" , False)
        fecha_start_2 = self.cleaned_data.get("time_start_curso")
        if not fecha_end:
            raise ValidationError("Por favor ingrese una fecha")
        if fecha_start_2 is None:
            raise ValidationError("La fecha de inicio es requerida correctamente")
        if fecha_end <= fecha_start_2:
            raise ValidationError(
                "No puede ingresar una fecha menor o igual a la de inicio")
        return fecha_end

    def clean_servicio_curso(self):
        servi = self.cleaned_data.get("servicio_curso",  False)
        if not servi:
            raise ValidationError("Por favor ingrese un Servicio")
        return servi

    def clean_hospital_curso(self):
        hosp = self.cleaned_data.get("hospital_curso",  False)
        if not hosp:
            raise ValidationError("Por favor ingrese un Hospital")
        return hosp

    def clean_personal_cursos(self):
        person = self.cleaned_data.get("personal_cursos",  False)
        if not person:
            raise ValidationError("Por favor Seleccione un personal")
        return person


class CreateNewHospital(forms.ModelForm):
    nombre_hospital = forms.CharField(max_length=70)

    class Meta:
        model = new_class_hospital
        exclude = ()

    def clean_nombre_hospital(self):
        nombre_hospital = self.cleaned_data.get("nombre_hospital",  False)
        if not nombre_hospital:
            raise ValidationError("Por favor ingrese un Hospital")
        if len(nombre_hospital) >= 71:
            raise ValidationError("Maximo 70 caracteres")
        return nombre_hospital


class CreateNewServcio(forms.ModelForm):
    nombre_sev = forms.CharField(max_length=50)
    class Meta:
        model = new_class_servicio
        exclude = ()

    def clean_nombre_sev(self):
        nombre_sev = self.cleaned_data.get("nombre_sev",  False)
        if not nombre_sev:
            raise ValidationError("Por favor ingrese un Servicio")
        if len(nombre_sev) >= 51:
            raise ValidationError("Maximo 50 caracteres")
        return nombre_sev


class CreateNewConsulta(forms.ModelForm):

    nombre_completo = forms.CharField(max_length=100)
    rut = forms.IntegerField()
    telefono = forms.IntegerField()
    Correo = forms.CharField(max_length=100)

    class Meta:
        model = create_new_consultas
        exclude = ()

    def clean_nombre_completo(self):
        nombre_completo = self.cleaned_data.get("nombre_completo",  False)
        if not nombre_completo:
            raise ValidationError("Por favor ingrese un nombre")
        if len(nombre_completo)>= 31:
            raise ValidationError("Maximo 30 caracteres")
        validador = str(nombre_completo).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        return nombre_completo
    
    def clean_rut(self):
        rut = self.cleaned_data.get("rut",  False)
        if not rut:
            raise ValidationError("Por favor ingrese un rut")
        if str(rut).isnumeric() == False:
            raise ValidationError("Solo ingrese numeros sin '.' , ni el digito verificador ")
        if len(str(rut)) >=9 and len(str(rut)) <=6 :
            raise ValidationError("rut invalido")
        return rut
        

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono",  False)
        if not telefono:
            raise ValidationError("Por favor ingrese un telefono")
        if str(telefono).isnumeric() == False:
            raise ValidationError("Solo ingrese numeros sin el +56")
        if len(str(telefono))  >=10:
            raise ValidationError("telefono invalido")
        return telefono
        
    def clean_Correo(self):
        Correo = self.cleaned_data.get("Correo",  False)
        EMAILS_FILE_TYPES = ['hotmail.com', 'hotmail.cl', 'gmail.com','outlook.cl','outlook.com']
        extension = str(Correo).split('@')[-1]
        file_type = extension.lower()
        if not Correo:
            raise ValidationError("Por favor ingrese un Correo")
        if file_type not in EMAILS_FILE_TYPES:
            raise ValidationError("Ingrese un Correo VALIDO personal")
        return Correo

class update_curso(forms.Form):
    curso_actualizar = forms.CharField(max_length=100)
    nombre_curso_up = forms.CharField(max_length=100)
    descrip_corta_curso = forms.CharField(max_length=250)
    img_curso_up = forms.ImageField(required=False)
    doc_curso_up = forms.FileField(required=False ) 
    descrip_larga_curso = forms.CharField(max_length=600)
    requisitos_curso = forms.CharField(max_length=100)
    time_start_curso = forms.DateField()
    time_end_curso = forms.DateField()
    servicio_curso = forms.CharField(max_length=100)
    hospital_curso = forms.CharField(max_length=100)
    personal_cursos = forms.CharField(max_length=80, required=False)

    def clean_doc_curso_up(self):
        DOCUMENTS_FILE_TYPES = ['docx', 'xlsx', 'pptx', 'pdf']
        uploaded_document = self.cleaned_data.get("doc_curso_up",  False)
        extension = str(uploaded_document).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_document:
            return uploaded_document
        if file_type not in DOCUMENTS_FILE_TYPES:
            raise ValidationError(
                "El archivo tiene que ser un documento de word o PDF.")
        return uploaded_document
    
    def clean_img_curso_up(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_curso_up",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            return uploaded_image
        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image


    def clean_nombre_curso_up(self):
        nombre = self.cleaned_data.get("nombre_curso_up",  False)
        print(nombre)
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre")
        if len(nombre) >= 71:
            raise ValidationError("Maximo 70 caracteres")
        return nombre

    

    def clean_descrip_corta_curso(self):
        descip_corta = self.cleaned_data.get("descrip_corta_curso",  False)
        if not descip_corta:
            raise ValidationError(
                "Por favor ingrese una descripción para precentar")
        if len(descip_corta) >= 201:
            raise ValidationError("Maximo 200 caracteres")
        return descip_corta

    def clean_descrip_larga_curso(self):
        descip_larga = self.cleaned_data.get("descrip_larga_curso",  False)
        if not descip_larga:
            raise ValidationError("Por favor ingrese una descripción")
        if len(descip_larga) >= 601:
            raise ValidationError("Maximo 600 caracteres")
        return descip_larga

    def clean_requisitos_curso(self):
        requisito = self.cleaned_data.get("requisitos_curso",  False)
        if not requisito:
            raise ValidationError(
                "Por favor ingrese Requisitos para aprobar curso")
        if len(requisito) >= 201:
            raise ValidationError("Maximo 200 caracteres")
        return requisito

    def clean_time_start_curso(self):
        fecha_start = self.cleaned_data.get("time_start_curso")
        hoy = datetime.datetime.now().date()
        if fecha_start is None:
            raise ValidationError("Por favor ingrese una fecha")
        if fecha_start < hoy:
            raise ValidationError("No se pueden ingresar fechas pasadas")
        return fecha_start

    def clean_time_end_curso(self):
        cleaned_data = super().clean()
        fecha_end = self.cleaned_data.get("time_end_curso" , False)
        fecha_start_2 = self.cleaned_data.get("time_start_curso")
        if not fecha_end:
            raise ValidationError("Por favor ingrese una fecha")
        if fecha_start_2 is None:
            raise ValidationError("La fecha de inicio es requerida correctamente")
        if fecha_end <= fecha_start_2:
            raise ValidationError(
                "No puede ingresar una fecha menor o igual a la de inicio")
        return fecha_end

    def clean_servicio_curso(self):
        servi = self.cleaned_data.get("servicio_curso",  False)
        if not servi:
            raise ValidationError("Por favor ingrese un Servicio")
        return servi

    def clean_hospital_curso(self):
        hosp = self.cleaned_data.get("hospital_curso",  False)
        if not hosp:
            raise ValidationError("Por favor ingrese un Hospital")
        return hosp

    def clean_personal_cursos(self):
        person = self.cleaned_data.get("personal_cursos",  False)
        if not person:
            raise ValidationError("Por favor Seleccione un personal")
        return person


class update_publicacion(forms.Form):
    id_update_pub = forms.CharField(max_length=100)
    nombre_pub = forms.CharField(max_length=100)
    descrip_pub = forms.CharField(max_length=100)
    img_pub_up = forms.ImageField(required=False)

    def clean_img_pub_up(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_pub_up",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            return uploaded_image
        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image
    
    def clean_nombre_pub(self):
        nombre = self.cleaned_data.get("nombre_pub")
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre")
        if len(nombre) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return nombre

    def clean_descrip_pub(self):
        descrip_pub = self.cleaned_data.get("descrip_pub")
        if not descrip_pub:
            raise ValidationError("Por favor ingrese una descripción")
        if len(descrip_pub) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return descrip_pub

    


class update_card(forms.Form):
    id_update = forms.CharField(max_length=100)
    nombre_card = forms.CharField(max_length=100)
    cargo_card = forms.CharField(max_length=100)
    descrip_card = forms.CharField(max_length=100)
    img_card_up = forms.ImageField(required=False)

    def clean_img_pub_up(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_card_up",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:
            return uploaded_image
        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image
    
    def clean_nombre_card(self):
        nombre = self.cleaned_data.get("nombre_card", False)
        if not nombre:
            raise ValidationError("Tiene que ingresar su nombre") 
        validador = str(nombre).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        if len(nombre) >= 26:
            raise ValidationError("Maximo 25 caracteres")
        return nombre

    def clean_cargo_card(self):
        cargo = self.cleaned_data.get("cargo_card")
        if not cargo:
            raise ValidationError("Tiene que ingresar un cargo")
        validador = str(cargo).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        if len(cargo) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return cargo

    def clean_descrip_card(self):
        descrip_card = self.cleaned_data.get("descrip_card")
        if not descrip_card:
            raise ValidationError("Tiene que ingresar un Nombre")
        if len(descrip_card) >= 101:
            raise ValidationError("Maximo 100 caracteres")
        return descrip_card

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    celular = forms.IntegerField()
    nombres = forms.CharField(max_length=70)

    class Meta:
        model = Usuario
        fields = ( 'username', 'password1', 'password2')

    def clean_nombres(self):
        nombre_completo = self.cleaned_data.get("nombres",  False)
        if not nombre_completo:
            raise ValidationError("Por favor ingrese un nombre")
        if len(nombre_completo)>= 31:
            raise ValidationError("Maximo 30 caracteres")
        validador = str(nombre_completo).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        return nombre_completo
    
    def clean_celular(self):
        celular = self.cleaned_data.get("celular",  False)
        if not celular:
            raise ValidationError("Por favor ingrese un numero")
        if str(celular).isnumeric() == False:
            raise ValidationError("Solo ingrese numeros sin el +56 ")
        if len(str(celular)) >=10 and len(str(celular)) <=8 :
            raise ValidationError("numero invalido")
        return celular
        
    def clean_email(self):
        Correo = self.cleaned_data.get("email",  False)
        EMAILS_FILE_TYPES = ['hotmail.com', 'hotmail.cl', 'gmail.com','outlook.cl','outlook.com']
        extension = str(Correo).split('@')[-1]
        file_type = extension.lower()
        if not Correo:
            raise ValidationError("Por favor ingrese un Correo")
        if file_type not in EMAILS_FILE_TYPES:
            raise ValidationError("Ingrese un Correo VALIDO personal")
        return Correo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class Update_user(forms.Form):
    id_update_user = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=100)
    celular = forms.IntegerField()
    nombres = forms.CharField(max_length=70)
    password = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput)
    username = forms.CharField(max_length=70)
    
    def clean_nombres(self):
        nombre_completo = self.cleaned_data.get("nombres",  False)
        if not nombre_completo:
            raise ValidationError("Por favor ingrese un nombre")
        if len(nombre_completo)>= 31:
            raise ValidationError("Maximo 30 caracteres")
        validador = str(nombre_completo).split(' ')[-1]
        if validador.isalpha() == False:
            raise ValidationError("Solo deben ser Letras")
        return nombre_completo
    
    def clean_celular(self):
        celular = self.cleaned_data.get("celular",  False)
        if not celular:
            raise ValidationError("Por favor ingrese un numero")
        if str(celular).isnumeric() == False:
            raise ValidationError("Solo ingrese numeros sin el +56 ")
        if len(str(celular)) >=10 and len(str(celular)) <=8 :
            raise ValidationError("numero invalido")
        return celular
        
    def clean_email(self):
        Correo = self.cleaned_data.get("email",  False)
        EMAILS_FILE_TYPES = ['hotmail.com', 'hotmail.cl', 'gmail.com','outlook.cl','outlook.com']
        extension = str(Correo).split('@')[-1]
        file_type = extension.lower()
        if not Correo:
            raise ValidationError("Por favor ingrese un Correo")
        if file_type not in EMAILS_FILE_TYPES:
            raise ValidationError("Ingrese un Correo VALIDO personal")
        return Correo



