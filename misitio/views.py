from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.shortcuts import redirect

cred = credentials.Certificate('./tottus-recetas-firebase.json')
default_app=firebase_admin.initialize_app(cred)
database = firestore.client()

def home_recetas(request):
    return render(request, 'view_html/index.html', {})

def actualizar_receta_id():

    my_ref = database.collection("listado_recetas")
    contador=0

    try:
        docs = my_ref.stream()
        for doc in docs:
            contador=contador+1
    except Exception as a:
        print(a)

    return contador+1

def actualizar_noticia_id():
    my_ref = database.collection("listado_noticias")
    contador=0

    try:
        docs = my_ref.stream()
        for doc in docs:
            contador=contador+1
    except Exception as a:
        print(a)

    return contador+1


def actualizar_consejos_id():
    my_ref = database.collection("listado_consejos")
    contador=0

    try:
        docs = my_ref.stream()
        for doc in docs:
            contador=contador+1
    except Exception as a:
        print(a)

    return contador+1

def actualizar_productos_id():
    my_ref = database.collection("listado_productos_dec")
    contador=0

    try:
        docs = my_ref.stream()
        for doc in docs:
            contador=contador+1
    except Exception as a:
        print(a)

    return contador+1


def actualizar_receta():
    my_ref = database.collection("listado_recetas")
    object_list=[]

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_receta'],'tit_ingredientes':doc.to_dict()['tit_ingredientes'],'tit_preparacion':doc.to_dict()['tit_preparacion'],'des_ingredientes':doc.to_dict()['des_ingredientes'],'des_preparacion':doc.to_dict()['des_preparacion']})
    except Exception as a:
        print(a)

    return object_list

def actualizar_noticia():
    my_ref = database.collection("listado_noticias")
    object_list=[]

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_noticia'],'url_image':doc.to_dict()['url_image']})
    except Exception as a:
        print(a)

    return object_list

def actualizar_consejos():
    my_ref = database.collection("listado_consejos")
    object_list=[]

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_noticia'],'url_image':doc.to_dict()['url_image']})
    except Exception as a:
        print(a)

    return object_list

def actualizar_productos():
    my_ref = database.collection("listado_productos")
    object_list=[]

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_noticia'],'url_image':doc.to_dict()['url_image']})
    except Exception as a:
        print(a)

    return object_list

def recetas_verifiqued_editar(request):
    if request.method=='POST' and 'editarrecetas' in request.POST:
        ideditar=request.POST['ideditar']
        user_=request.POST['user_id']
        print("edit " + ideditar)
        doc_ref = database.collection("listado_recetas").document(ideditar)
        mensaje=""
        object_list=[]

        try:
            doc = doc_ref.get()
            idcodigo=doc.id
            titulo=doc.to_dict()['nombre_receta']
            urlimage=doc.to_dict()['url_image']
            titulo_ingredientes=doc.to_dict()['tit_ingredientes']
            desarrollo_ingredientes=doc.to_dict()['des_ingredientes']
            titulo_preparacion=doc.to_dict()['tit_preparacion']
            desarrollo_preparacion=doc.to_dict()['des_preparacion']
            
        except Exception as a:
            print(a)

        visibleedit='block'

        data={
            'usuario':user_,
            'idrecetaedit':idcodigo,
            'tituloedit':titulo,
            'urlimgedit':urlimage,
            'titulo_ingredientesedit':titulo_ingredientes,
            'desarrollo_ingredientesedit':desarrollo_ingredientes,
            'titulo_preparacionedit':titulo_preparacion,
            'desarrollo_preparacionedit':desarrollo_preparacion,
            'mensaje': mensaje,
            'object_list':actualizar_receta(),
            'idreceta':actualizar_receta_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/recetas.html', data)
    
    if request.method=='POST' and 'editarrecetasoficial' in request.POST:
        print("Update....")
        visibleedit='none'

        ideditar=request.POST['idrecetaedit']
        print("id product " + ideditar)
        doc_ref_edit = database.collection("listado_recetas").document(ideditar)

        titulo=request.POST['tituloedit']
        urlimg=request.POST['urlimgedit']
        titulo_ingredientes=request.POST['titulo_ingredientesedit']
        desarrollo_ingredientes=request.POST['desarrollo_ingredientesedit']
        titulo_preparacion=request.POST['titulo_preparacionedit']
        desarrollo_preparacion=request.POST['desarrollo_preparacionedit']

        print("prueba " + titulo +" " + urlimg+" "+titulo_ingredientes+" "+desarrollo_ingredientes+" "+titulo_preparacion+" "+desarrollo_preparacion)

        try:
            doc_ref_edit.update({'nombre_receta': titulo, 'url_image': urlimg,'tit_ingredientes':titulo_ingredientes,'des_ingredientes':desarrollo_ingredientes,'tit_preparacion':titulo_preparacion,'des_preparacion':desarrollo_preparacion})
            mensaje="Se actualizo correctamente"
        except Exception as a:
            mensaje="No se pudo actualizar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_receta(),
            'idreceta':actualizar_receta_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/recetas.html', data)
    
    if request.method=='POST' and 'deleterecetas' in request.POST:
        print("delete")
        visibleedit='none'

        idreceta=request.POST['codigo']
        try:
            doc_ref = database.collection("listado_recetas").document(str(idreceta))
            doc_ref.delete()
            mensaje="Se elimino correctamente"
        except Exception as a:
            mensaje="No se pudo eliminar, vuelva a intentarlo"
            print(a)
        
        data={
            'mensaje': mensaje,
            'object_list':actualizar_receta(),
            'idreceta':actualizar_receta_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/recetas.html', data)
    
    if request.method=='POST' and 'saverecetas' in request.POST:
        visibleedit='none'
        idreceta=request.POST['idreceta']

        my_ref = database.collection("listado_recetas").document(str(idreceta))

        titulo=request.POST['titulo']
        urlimg=request.POST['urlimg']
        titulo_ingredientes=request.POST['titulo_ingredientes']
        desarrollo_ingredientes=request.POST['desarrollo_ingredientes']
        titulo_preparacion=request.POST['titulo_preparacion']
        desarrollo_preparacion=request.POST['desarrollo_preparacion']
       
        try:
            my_ref.set({u'nombre_receta': titulo, u'url_image': urlimg,u'tit_ingredientes':titulo_ingredientes,u'des_ingredientes':desarrollo_ingredientes,u'tit_preparacion':titulo_preparacion,u'des_preparacion':desarrollo_preparacion})
            mensaje="Se guardo correctamente"
        except Exception as a:
            mensaje="No se pudo guardar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_receta(),
            'idreceta':actualizar_receta_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/recetas.html', data)

def recetas(request,user_):
    mensaje=""
    my_ref = database.collection("listado_recetas")
    object_list=[]
    contador=0
    idreceta=0
    visibleedit='none'

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_receta'],'tit_ingredientes':doc.to_dict()['tit_ingredientes'],'tit_preparacion':doc.to_dict()['tit_preparacion'],'des_ingredientes':doc.to_dict()['des_ingredientes'],'des_preparacion':doc.to_dict()['des_preparacion']})
            contador=contador+1
    except Exception as a:
        print(a)

    try:
        print("# of documents in collection: {} " + str(contador))
        idreceta=contador+1
    except Exception as a:
            print(a)
    
    data={
        'mensaje': mensaje,
        'object_list':object_list,
        'idreceta':idreceta,
        'none':visibleedit,
        'usuario':user_
    }

    return render(request, 'view_html/recetas.html', data)

def noticias_verifiqued(request):
    if request.method=='POST' and 'editarnoticiasoficial' in request.POST:
        print("Update....")
        visibleedit='none'

        ideditar=request.POST['idrecetaedit']
        print("id product " + ideditar)
        doc_ref_edit = database.collection("listado_noticias").document(ideditar)

        titulo=request.POST['tituloedit']
        urlimg=request.POST['urlimgedit']

        try:
            doc_ref_edit.update({'nombre_noticia': titulo, 'url_image': urlimg})
            mensaje="Se actualizo correctamente"
        except Exception as a:
            mensaje="No se pudo actualizar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)


    if request.method=='POST' and 'editarnoticias' in request.POST:
        visibleedit='block'
        user_=request.POST['user_id']
        ideditar=request.POST['ideditar']
        doc_ref = database.collection("listado_noticias").document(ideditar)
        mensaje=""
        object_list=[]

        try:
            doc = doc_ref.get()
            idcodigo=doc.id
            titulo=doc.to_dict()['nombre_noticia']
            urlimage=doc.to_dict()['url_image']
        except Exception as a:
            print(a)

        data={
            'usuario':user_,
            'idrecetaedit':idcodigo,
            'tituloedit':titulo,
            'urlimgedit':urlimage,
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)
    
    if request.method=='POST' and 'deletenoticias' in request.POST:
        print("delete")
        visibleedit='none'

        idreceta=request.POST['codigo']
        try:
            doc_ref = database.collection("listado_noticias").document(str(idreceta))
            doc_ref.delete()
            mensaje="Se elimino correctamente"
        except Exception as a:
            mensaje="No se pudo eliminar, vuelva a intentarlo"
            print(a)
        
        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)
    
    if request.method=='POST' and 'savenoticias' in request.POST:
        visibleedit='none'
        idreceta=request.POST['idnoticia']

        my_ref = database.collection("listado_noticias").document(str(idreceta))

        titulo=request.POST['titulo']
        urlimg=request.POST['urlimg']
       
        try:
            my_ref.set({u'nombre_noticia': titulo, u'url_image': urlimg})
            mensaje="Se guardo correctamente"
        except Exception as a:
            mensaje="No se pudo guardar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)

def noticias(request,user_):
    visibleedit='none'
    mensaje=""
    idnoticia=0
    my_ref = database.collection("listado_noticias")
    object_list=[]
    contador=0

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_noticia']})
            contador=contador+1
    except Exception as a:
        print(a)

    try:
        print("# of documents in collection: {} " + str(contador))
        idnoticia=contador+1
    except Exception as a:
            print(a)

    if request.method=='POST' and 'saverecetas' in request.POST:
       
        titulo_not=request.POST['titulo_not']
        urlimg_not=request.POST['urlimg_not']

    data={
        'mensaje': mensaje,
        'object_list':object_list,
        'idnoticia':idnoticia,
        'none':visibleedit,
        'usuario':user_
    }

    return render(request, 'view_html/noticias.html', data)

def consejos_verifiqued(request):
    if request.method=='POST' and 'editarconsejossoficial' in request.POST:
        print("Update....")
        visibleedit='none'

        ideditar=request.POST['idrecetaedit']
        print("id product " + ideditar)
        doc_ref_edit = database.collection("listado_consejos").document(ideditar)

        titulo=request.POST['tituloedit']
        urlimg=request.POST['urlimgedit']

        try:
            doc_ref_edit.update({'nombre_consejos': titulo, 'url_image': urlimg})
            mensaje="Se actualizo correctamente"
        except Exception as a:
            mensaje="No se pudo actualizar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_consejos(),
            'idconsejo':actualizar_consejos_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/consejos.html', data)


    if request.method=='POST' and 'editarconsejos' in request.POST:
        visibleedit='block'
        user_=request.POST['user_id']
        ideditar=request.POST['ideditar']
        doc_ref = database.collection("listado_consejos").document(ideditar)
        mensaje=""
        object_list=[]

        try:
            doc = doc_ref.get()
            idcodigo=doc.id
            titulo=doc.to_dict()['nombre_consejo']
            urlimage=doc.to_dict()['url_image']
        except Exception as a:
            print(a)

        data={
            'usuario':user_,
            'idrecetaedit':idcodigo,
            'tituloedit':titulo,
            'urlimgedit':urlimage,
            'mensaje': mensaje,
             'object_list':actualizar_consejos(),
            'idconsejo':actualizar_consejos_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/consejos.html', data)
    
    if request.method=='POST' and 'deleteconsejos' in request.POST:
        print("delete")
        visibleedit='none'

        idreceta=request.POST['codigo']
        try:
            doc_ref = database.collection("listado_noticias").document(str(idreceta))
            doc_ref.delete()
            mensaje="Se elimino correctamente"
        except Exception as a:
            mensaje="No se pudo eliminar, vuelva a intentarlo"
            print(a)
        
        data={
            'mensaje': mensaje,
             'object_list':actualizar_consejos(),
            'idconsejo':actualizar_consejos_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)
    
    if request.method=='POST' and 'savenoticias' in request.POST:
        visibleedit='none'
        idreceta=request.POST['idnoticia']

        my_ref = database.collection("listado_noticias").document(str(idreceta))

        titulo=request.POST['titulo']
        urlimg=request.POST['urlimg']
       
        try:
            my_ref.set({u'nombre_noticia': titulo, u'url_image': urlimg})
            mensaje="Se guardo correctamente"
        except Exception as a:
            mensaje="No se pudo guardar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_consejos(),
            'idconsejo':actualizar_consejos_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/consejos.html', data)

def consejos(request,user_):
    visibleedit='none'
    mensaje=""
    idconsejo=0
    my_ref = database.collection("listado_consejos")
    object_list=[]
    contador=0

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_consejos'],'url_image':doc.to_dict()['url_image'],'texto_consejo':doc.to_dict()['texto_consejo']})
            contador=contador+1
    except Exception as a:
        print(a)

    try:
        print("# of documents in collection: {} " + str(contador))
        idconsejo=contador+1
    except Exception as a:
            print(a)

    data={
        'mensaje': mensaje,
        'object_list':object_list,
        'idconsejo':idconsejo,
        'none':visibleedit,
        'usuario':user_
    }

    return render(request, 'view_html/consejos.html', data)

def productos_verifiqued(request):
    if request.method=='POST' and 'editarnoticiasoficial' in request.POST:
        print("Update....")
        visibleedit='none'

        ideditar=request.POST['idrecetaedit']
        print("id product " + ideditar)
        doc_ref_edit = database.collection("listado_noticias").document(ideditar)

        titulo=request.POST['tituloedit']
        urlimg=request.POST['urlimgedit']

        try:
            doc_ref_edit.update({'nombre_noticia': titulo, 'url_image': urlimg})
            mensaje="Se actualizo correctamente"
        except Exception as a:
            mensaje="No se pudo actualizar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)


    if request.method=='POST' and 'editarnoticias' in request.POST:
        visibleedit='block'
        user_=request.POST['user_id']
        ideditar=request.POST['ideditar']
        doc_ref = database.collection("listado_noticias").document(ideditar)
        mensaje=""
        object_list=[]

        try:
            doc = doc_ref.get()
            idcodigo=doc.id
            titulo=doc.to_dict()['nombre_noticia']
            urlimage=doc.to_dict()['url_image']
        except Exception as a:
            print(a)

        data={
            'usuario':user_,
            'idrecetaedit':idcodigo,
            'tituloedit':titulo,
            'urlimgedit':urlimage,
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)
    
    if request.method=='POST' and 'deletenoticias' in request.POST:
        print("delete")
        visibleedit='none'

        idreceta=request.POST['codigo']
        try:
            doc_ref = database.collection("listado_noticias").document(str(idreceta))
            doc_ref.delete()
            mensaje="Se elimino correctamente"
        except Exception as a:
            mensaje="No se pudo eliminar, vuelva a intentarlo"
            print(a)
        
        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/noticias.html', data)
    
    if request.method=='POST' and 'savenoticias' in request.POST:
        visibleedit='none'
        idreceta=request.POST['idnoticia']

        my_ref = database.collection("listado_noticias").document(str(idreceta))

        titulo=request.POST['titulo']
        urlimg=request.POST['urlimg']
       
        try:
            my_ref.set({u'nombre_noticia': titulo, u'url_image': urlimg})
            mensaje="Se guardo correctamente"
        except Exception as a:
            mensaje="No se pudo guardar, vuelva a intentarlo"
            print(a)

        data={
            'mensaje': mensaje,
            'object_list':actualizar_noticia(),
            'idnoticia':actualizar_noticia_id(),
            'none':visibleedit
        }

        return render(request, 'view_html/productos.html', data)

def productos(request,user_):
    visibleedit='none'
    mensaje=""
    idnoticia=0
    my_ref = database.collection("listado_productos")
    object_list=[]
    contador=0

    try:
        docs = my_ref.stream()
        
        for doc in docs:
            object_list.append({'idcodigo':doc.id,'nombre':doc.to_dict()['nombre_consejos'],'url_image':doc.to_dict()['url_image'],'texto_consejo':doc.to_dict()['texto_consejo']})
            contador=contador+1
    except Exception as a:
        print(a)

    try:
        print("# of documents in collection: {} " + str(contador))
        idconsejo=contador+1
    except Exception as a:
            print(a)

    data={
        'mensaje': mensaje,
        'object_list':object_list,
        'idconsejo':idconsejo,
        'none':visibleedit,
        'usuario':user_
    }

    return render(request, 'view_html/consejos.html', data)

def login(request):
    data={}
    mensaje=""

    if request.method=='POST' and 'cerrar' in request.POST:
        print("Cerrando sesión... ")
        return render(request, 'view_html/login.html', {})


    if request.method=='POST' and 'iniciar' in request.POST:
        print("Iniciando sesión... ")
        user=request.POST['usuario']
        password=request.POST['pass']
        mensaje=""

        print("Bienvenido.. " + user)

        try:
            my_ref_user =database.collection("users").where('usuario', '==', user).stream()
            my_ref_pass =database.collection("users").where('pass', '==',password).stream()
            if my_ref_user and  my_ref_pass:
                for doc in my_ref_user:
                    return redirect('/home/recetas/'+user)
        except Exception as a:
            print("Error no coinciden o ocurrió el siguiente error: " + str(a))
        
        mensaje="No coinciden usuario y contraseña"
    
    data={
        'mensaje':mensaje
    }
        
    return render(request, 'view_html/login.html', data)

def save_consejos(request):
    if request.method=='POST' and 'saverecetas' in request.POST:
       
        titulo_con=request.POST['titulo_con']
        urlimg_con=request.POST['urlimg_con']

    return render(request, 'view_html/index.html', {})

