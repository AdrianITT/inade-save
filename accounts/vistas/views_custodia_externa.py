from accounts.models import Contenedor,Preservador,prioridad,Matriz,prioridad,outer_chain_row,info_cliente,unidad_medida,inte_matriz,inte_parametro_analitico,inte_perservador,cadena_externa,parametro_analitico,claves
from accounts.forms import crear_custodia_externa
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator

#   VISTA PARA DIRIGIR A GUIA DE OPERACIONES
from django.shortcuts import render, redirect

#    ABRIR CUSTODIA EXTERNA
def custodias(request):

    outer_chain_rows=outer_chain_row.objects.all()
    cadena_externas=cadena_externa.objects.all()

    context = {
        'outer_chain_rows':outer_chain_rows,
        'cadena_externas':cadena_externas,
    }

    return render(request, 'accounts/custodiaExterna/cadena_custodia_externa_inicio.html', context)

# CREAR CUSTODIA EXTERNA
def crear_custodia_externa(request):
    
    if request.method == 'POST':
        
        # Crear un nuevo objeto de info_cliente
        cliente_obj = info_cliente.objects.create(
            razon_social=request.POST['razon_social'],
            direccion_cliente=request.POST['direccion'],
            contacto_cliente=request.POST['contacto'],
            puesto_cargo=request.POST['puesto_cargo'],
        )
        
        #formato de id OT
        fecha_id_laboratorio=request.POST['id_orden de trabajo']
        numero_id_laboratorio=int(request.POST['numero_trabajo'])
        fecha_id_laboratorio_datetime = datetime.strptime(fecha_id_laboratorio, "%Y-%m-%d")
        year_id=fecha_id_laboratorio_datetime.year
        month_id=fecha_id_laboratorio_datetime.month
        day_id=fecha_id_laboratorio_datetime.day
        
        #formato de id OT
        year_format=f"{year_id % 100:02d}"
        month_format= f"{month_id:02d}"
        day_format= f"{day_id:02d}"
        numeri_id_lab= f"{numero_id_laboratorio:02d}"
        
        #formato orden de trabajo
        order_format=f"{year_format}{month_format}{day_format}-{numeri_id_lab}"
        

        # Crear el objeto de cadena_externa primero
        cadena_externa_obj = cadena_externa.objects.create(
            id_inforclient=cliente_obj,
            id_orden_trabajo=order_format,)  # Crea el objeto cadena_externa
        
        # Crear un nuevo objeto de outer_chain_row
        #outer_chain = outer_chain_row.objects.create(
        #    ce=cadena_externa_obj,
        #)
        
        '''
        # Crear un nuevo objeto de outer_chain_row
        outer_chain = outer_chain_row.objects.create(
            id_ce=cadena_externa_obj,  # Aquí estamos vinculando la llave foránea
            id_orden_trabajo=request.POST['id_orden_trabajo'],
            id_inforclient=cliente_obj,
            # Otros campos de outer_chain_row
        )'''
        

        # Guardar el objeto outer_chain_row
        cadena_externa_obj.save()
        

        # Redirigir a una página de éxito
        return redirect('custodia_acep')
    
    return render(request, 'custodia_acep')

#MUESTRA LAS FILAS DE LA VISTA row_custodia_externa.html
def row_custodia_externa(request, id_ce):
    rows = cadena_externa.objects.filter(ce=id_ce)
    #PENDIENTE PAGINACION
    desplay_rows= outer_chain_row.objects.filter(ce=id_ce, complet=False).order_by('datetime_muestreo')
    desplay_rows_complet= outer_chain_row.objects.filter(ce=id_ce, complet=True).order_by('datetime_muestreo')
    paginator = Paginator(desplay_rows, 5)
    paginator_complet=Paginator(desplay_rows_complet, 5)  
    page_number = request.GET.get('page') 
    page_number_complet=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj_complet=paginator_complet.get_page(page_number_complet)
    
    request.session['id_ce'] = id_ce#se guarda en memoria
    matrices=Matriz.objects.all()
    contenedores = Contenedor.objects.all()
    preservadores = Preservador.objects.all()
    prioridades = prioridad.objects.all()
    #outer_chain_rows=outer_chain_row.objects.all()
    parametro_analiticos=parametro_analitico.objects.all()
    cadena_externas= cadena_externa.objects.all()
    claves_row=claves.objects.all()

    contexts = {
        'claves_row':claves_row,
        'page_obj':page_obj,
        'page_obj_complet':page_obj_complet,
        'rows':rows,
        'matrices':matrices,
        'contenedores': contenedores,
        'preservadores': preservadores,
        'prioridades': prioridades,
        'desplay_rows':desplay_rows,
        'parametro_analiticos':parametro_analiticos,
        'cadena_externas':cadena_externas,
    }
 
    return render(request,'accounts/custodiaExterna/row_custodia_externa.html',contexts)

def row_datos_custodia(request):
    # Recuperar id_ce desde la sesión
    id_ce = request.session.get('id_ce', None)
    
    if id_ce is None:
        # Maneja el caso si no se encuentra el id_ce en la sesión
        return redirect('custodia_acep')  # O lo que consideres adecuado
    
    # Ahora puedes usar id_ce para obtener el objeto correspondiente
    cadena_externa_obj = cadena_externa.objects.get(ce=id_ce)
    
    if request.method=='POST':

        unidad=unidad_medida.objects.create(
            medida=request.POST['volumen_cantidad']
        )
    
        # Crear un nuevo objeto de outer_chain_row
        contenedor_id = request.POST['contenedor']
        contenedor = Contenedor.objects.get(id=contenedor_id)
        
        datetime_muestreo_str = request.POST['datetime_muestreo']
        datetime_muestreo = datetime.strptime(datetime_muestreo_str, '%Y-%m-%d')  # Convierte la cadena a un objeto datetime
        #horafinal_str=request.POST['hora_final']
        #horafinal=datetime.strptime(horafinal_str, '%H:%M')
        
        # Obtener los valores del formulario
        claves_row_id = request.POST.get('claves_row')
        claves_row= claves.objects.get(id=claves_row_id)
        number = request.POST.get('number')
        letra_row = request.POST.get('letra_row')
        claves_row_instance = claves.objects.get(id=request.POST['claves_row'])

        # Concatenar los valores en una sola cadena
        concatenated_value = f"{claves_row.name_clave}-{number}-{letra_row}"
        
        #formato de id laboratorio
        fecha_id_laboratorio=request.POST['id_laborratorio']
        numero_id_laboratorio=int(request.POST['numero_laboratorio'])
        fecha_id_laboratorio_datetime = datetime.strptime(fecha_id_laboratorio, "%Y-%m-%d")
        year_id=fecha_id_laboratorio_datetime.year
        month_id=fecha_id_laboratorio_datetime.month
        day_id=fecha_id_laboratorio_datetime.day
        
        #formato de id laboratorio
        year_format=f"{year_id % 100:02d}"
        month_format= f"{month_id:02d}"
        day_format= f"{day_id:02d}"
        numeri_id_lab= f"{numero_id_laboratorio:02d}"
        
        #formato final
        end_format=f"{year_format}{month_format}{day_format}-{numeri_id_lab}"
        
        outer_chain=outer_chain_row.objects.create(
            ce=cadena_externa_obj, # Aquí estamos vinculando la llave foránea
            datetime_muestreo=datetime_muestreo,  # Asignamos la fecha y hora seleccionada
            #horafinal=horafinal,
            id_laboratorio=end_format,
            id_filtor=request.POST['id_filtro'],
            origen_muestra=request.POST['origen_muestra'],
            id_contenedor = contenedor,
            iunidad_medida=unidad,
            identificador_campo=concatenated_value,
            id_clave=claves_row,
            # Otros campos de outer_chain_row
        )
        
        # Guardar los preservadores seleccionados
        preservador_seleccionado = request.POST.getlist('preservadores[]')  # Obtiene los IDs de los preservadores seleccionados
        for preservador_id in preservador_seleccionado:
            preservador = Preservador.objects.get(id=preservador_id)
            inte_perservador.objects.create(
                externa_row=outer_chain,
                preservador=preservador
            )  # Relaciona el preservador con el outer_chain_row
        # Guardar las matrices seleccionadas
        matriz_seleccionada = request.POST.getlist('matrices[]')  # Obtiene los IDs de las matrices seleccionadas
        for matriz_id in matriz_seleccionada:
            matriz = Matriz.objects.get(id=matriz_id)
            inte_matriz.objects.create(
                externa_row=outer_chain,
                matriz=matriz
            )  # Relaciona la matriz con el outer_chain_row
        # Guardar la prioridad seleccionada (relación ForeignKey)
        prioridad_seleccionada = request.POST['id_prioridad']
        prioridad_obj = prioridad.objects.get(id=prioridad_seleccionada)
        outer_chain.id_prioridad = prioridad_obj
        
        int_parametro_analitico=request.POST.getlist('parametro_analiticos[]')
        for parametro_id in int_parametro_analitico:
            parametro=parametro_analitico.objects.get(id=parametro_id)
            inte_parametro_analitico.objects.create(
                parametro_analitico=parametro,
                externa_row=outer_chain,
            )

        # Guardar el objeto outer_chain_row
        outer_chain.save()
        return redirect('row_custodia_externa', id_ce=id_ce)
    
    return render(request,'custodia_acep')

#MUESTRA DETALLES DE CADA FILA
def row_detalles(request, id_outer_chain):
    rows=outer_chain_row.objects.filter(externa_row=id_outer_chain)
    int_matriz_row=inte_matriz.objects.filter(externa_row=id_outer_chain)
    int_perservador=inte_perservador.objects.filter(externa_row=id_outer_chain)
    int_parametro_analitico=inte_parametro_analitico.objects.filter(externa_row=id_outer_chain)
    matriz_rows = Matriz.objects.filter(id__in=[matriz.matriz.id for matriz in int_matriz_row])
    perservador_rows=Preservador.objects.filter(id__in=[preservador.preservador.id for preservador in int_perservador])
    parametro_analitico_rows=parametro_analitico.objects.filter(id__in=[parametro_analitico.parametro_analitico.id for parametro_analitico in int_parametro_analitico])
    contenedor_rows=Contenedor.objects.filter(id=id_outer_chain)

    context={
        'rows':rows,
        'matriz_rows':matriz_rows,
        'int_matriz_row':int_matriz_row,
        'perservador_rows':perservador_rows,
        'parametro_analitico_rows':parametro_analitico_rows,
        'contenedor_rows':contenedor_rows,
    }
    
    return render(request,'accounts/custodiaExterna/cadena_cuatodia_externa_detalles.html',context)

def end_external_custody(request,id_outer_chain):
    #horafinal_str = datetime.now()
    horafinal_str=request.POST['hora_final']
    # Formatear la hora actual como una cadena
    if horafinal_str:
        # Convierte la cadena de hora a un objeto datetime
        horafinal = datetime.strptime(horafinal_str, "%H:%M").strftime("%H:%M")
    else:
        return print("Hora final no proporcionada.", status=400)
    outer_chain_row.objects.filter(externa_row=id_outer_chain).update(complet=True,horafinal=horafinal)
    outer_chain=outer_chain_row.objects.filter(externa_row=id_outer_chain).first()
    ce = outer_chain.ce.pk

    data=row_custodia_externa(request,ce)
    return data




