from django.shortcuts import render
from . import conection
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from . import views

def login(request):
    if request.method=='POST' and 'iniciar' in request.POST:
        print("Iniciando sesión... ")
        user=request.POST['usuario']
        password=request.POST['pass']
        mensaje=""

        print("Bienvenido.. " + user)
        cred = credentials.Certificate('./tottus-recetas-firebase.json')
        default_app=firebase_admin.initialize_app(cred)
        database = firestore.client()

        try:
            my_ref =database.collection("users").where(u'usuario', u'==', user).stream()
            data={
                'usuario':user
            }
            #views.recetas()
            #return render(request, 'view_html/recetas.html', data)

        except Exception as a:
            print("Error no coinciden o ocurrió el siguiente error: " + a)
            mensaje="No coinciden usuario o contraseña"
            data={
                'mensaje':mensaje
            }
            return render(request, 'view_html/login.html', data)
        
    return render(request, 'view_html/login.html', {})