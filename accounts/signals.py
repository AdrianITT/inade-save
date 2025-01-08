# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals  # Importar aquí

# accounts/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Metodo, Matriz, Contenedor, claves, sample_type, parametro_analitico,prioridad,Preservador

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if sender.name == 'accounts':
        # Crear nuevos registros en la tabla Metodo
        Metodo.objects.bulk_create([
            Metodo(metodo='NOM-011-STPS-2001'),
            Metodo(metodo='NOM-015-STPS-2001'),
            Metodo(metodo='NOM-022-STPS-2015'),
            Metodo(metodo='NOM-025-STPS-2008'),
            Metodo(metodo='NOM-010-STPS-2014'),
            Metodo(metodo='NOM-081-SEMARNAT-1994'),
        ], ignore_conflicts=True)  # Agregar ignore_conflicts para evitar duplicados
        Preservador.objects.bulk_create([
            Preservador(name_perservador='Hielo'),
            Preservador(name_perservador='ácido tetraoxosulfúrico'),
            Preservador(name_perservador='ácido clorhídrico'),
            Preservador(name_perservador='ácido trioxonítrico'),
            Preservador(name_perservador='anión de dicromato'),
            Preservador(name_perservador='hidróxido de sodio'),
            Preservador(name_perservador='ácido nítrico '),
            Preservador(name_perservador='Otros'),
            Preservador(name_perservador='No Aplica'),
        ])
        
        Matriz.objects.bulk_create([
            Matriz(letra_matriz='S'),
            Matriz(letra_matriz='L'),
            Matriz(letra_matriz='G'),
            Matriz(letra_matriz='O')
        ],ignore_conflicts=True)
        
        Contenedor.objects.bulk_create([
            Contenedor(letra_contenedor='V',name_contenedor='vidrio claro'),
            Contenedor(letra_contenedor='F',name_contenedor='Filtro'),
            Contenedor(letra_contenedor='A',name_contenedor='Vidrio ambar'),
            Contenedor(letra_contenedor='B',name_contenedor='Bolsa'),
            Contenedor(letra_contenedor='P',name_contenedor='Plastico'),
            Contenedor(letra_contenedor='O',name_contenedor='Otros')
        ],ignore_conflicts=True)
        
        claves.objects.bulk_create([
            claves(name_clave='AR'),
            claves(name_clave='AP'),
            claves(name_clave='EM'),
            claves(name_clave='AL'),
            claves(name_clave='O')
        ],ignore_conflicts=True)
        
        sample_type.objects.bulk_create([
            sample_type(name_type='MP'),
            sample_type(name_type='MC')
        ],ignore_conflicts=True)
        
        prioridad.objects.bulk_create([
            prioridad(categoria='A', day='15',day_min='15'),
            prioridad(categoria='B', day='10',day_min='8'),
            prioridad(categoria='C', day='5',day_min='3')
        ])
        
        parametro_analitico.objects.bulk_create([
            parametro_analitico(opcin_analitic='Grasas y aceites'),
            parametro_analitico(opcin_analitic='Solidos sedimentables'),
            parametro_analitico(opcin_analitic='DQO'),
            parametro_analitico(opcin_analitic='Solidos y Sales Disueltas en Aguas'),
            parametro_analitico(opcin_analitic='pH'),
            parametro_analitico(opcin_analitic='Conductividad'),
            parametro_analitico(opcin_analitic='Mentales Disueltos y suspendidos'),
            parametro_analitico(opcin_analitic='Metales Totales Genericos'),
            parametro_analitico(opcin_analitic='Mercurio'),
            parametro_analitico(opcin_analitic='Arsenico'),
            parametro_analitico(opcin_analitic='Sulfatos'),
            parametro_analitico(opcin_analitic='Cromo VI'),
            parametro_analitico(opcin_analitic='Nitratos'),
            parametro_analitico(opcin_analitic='Nitritos'),
            parametro_analitico(opcin_analitic='Fosforo Total'),
            parametro_analitico(opcin_analitic='Cianuros Totales'),
            parametro_analitico(opcin_analitic='Acidez y Alcalinidad'),
            parametro_analitico(opcin_analitic='Cloruros'),
            parametro_analitico(opcin_analitic='DBO'),
            parametro_analitico(opcin_analitic='Dureza Total'),
            parametro_analitico(opcin_analitic='Oxigeno Disuelto'),
            parametro_analitico(opcin_analitic='Turbidez'),
            parametro_analitico(opcin_analitic='Fenoles'),
            parametro_analitico(opcin_analitic='Fluoruros'),
            parametro_analitico(opcin_analitic='Nitrogeno Total Kjeldahl'),
            parametro_analitico(opcin_analitic='Temperatura'),
            parametro_analitico(opcin_analitic='SAAM'),
            parametro_analitico(opcin_analitic='Coniformes Totales y Fecales'),
            parametro_analitico(opcin_analitic='Olor'),
            parametro_analitico(opcin_analitic='Cloro Total')
        ],ignore_conflicts=True)
