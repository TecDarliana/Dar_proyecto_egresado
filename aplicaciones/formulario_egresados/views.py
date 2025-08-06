from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages # Asegúrate de que esta línea esté presente
import requests
import json
from aplicaciones.formulario_egresados.forms import *
from aplicaciones.formulario_egresados.models import *

def datos_personales_egresado(request):
    if request.method == 'POST':
        personal_form = datos_pesonales_formModel(request.POST)
        academic_form = datos_academicos_formModel(request.POST)

        if personal_form.is_valid() and academic_form.is_valid():
            try:
                datos_personales = personal_form.save()
                datos_academicos = academic_form.save(commit=False)
                datos_academicos.becario = datos_personales
                datos_academicos.save()
                
                # ⚡️ Generar un mensaje de éxito ⚡️
                messages.success(request, 'El registro se agregó con éxito.')
                
                # ⚡️ Redirigir a la misma URL para un nuevo registro ⚡️
                # Usar el nombre de la URL ('registro') en lugar del nombre del archivo
                return redirect('registro') 
            except Exception as e:
                messages.error(request, f'Ocurrió un error al guardar los datos: {e}')
                # Si hay un error, el formulario se vuelve a mostrar con los datos y errores
        else:
            # Si el formulario no es válido, los errores se muestran automáticamente
            messages.warning(request, 'Por favor, corrige los errores en el formulario.')

    # Si es una solicitud GET o si la validación falla, se renderiza el formulario
    else:
        personal_form = datos_pesonales_formModel()
        academic_form = datos_academicos_formModel()

    context = {
        'personal_form': personal_form,
        'academic_form': academic_form,
    }
    return render(request, 'form-becarios.html', context)

# La vista 'consultar_cedula_json' no necesita cambios y funciona como antes.
def consultar_cedula_json(request):
    # ... (código existente) ...
    # No necesita cambios para este requerimiento
    nacionalidad = request.GET.get('nacionalidad')
    cedula = request.GET.get('cedula')
    
    if not nacionalidad or not cedula:
        return JsonResponse({'error': "Se requieren los parámetros 'nacionalidad' y 'cedula'."}, status=400)

    url = "https://comunajoven.com.ve/api/cedula"
    params = {'nacionalidad': nacionalidad, 'cedula': cedula}
    headers = {
        'Authorization': 'Bearer faa3dc480981bbfb734839367d2c9367',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = json.loads(response.content.decode('utf-8-sig'))
        return JsonResponse(data, status=200, safe=False)
    except requests.exceptions.HTTPError as e:
        return JsonResponse({'error': f"Error HTTP al consultar la API: {e}"}, status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)