import Moodle as api
import json

import os
from babel.dates import format_datetime
import datetime
import pytz



# Zona horaria de Ecuador
ecuador_tz = pytz.timezone('America/Guayaquil')

#Obtener materias

def Obtener_tareas(token, userId, link):

    materias = api.getMaterias(token, userId, link)    

    output = {}

    for materia in materias:
        nombreMateria = materia['fullname'].split('-')[0]
        output[nombreMateria] = {}

        #Obtenemos las tareas de cada curso
        tareas = api.getAssignments(token, materia['id'], link)
        tareas = tareas['courses'][0]['assignments']

        for tarea in tareas:
            
            
            #Fecha
            output[nombreMateria][tarea['name']] = tarea['duedate']

        #Obtenemos los quizes de cada curso
        quizes = api.getQuizes(token, materia['id'], link)
        quizes = quizes['quizzes']

        for quiz in quizes:
            #Fecha
            output[nombreMateria][quiz['name']] = quiz['timeclose']

        
        #Obtenemos los foros de cada curso
        foros = api.getForums(token, materia['id'], link)
        

        for foro in foros:
            if foro['duedate']:
                #Fecha
                output[nombreMateria][foro['name']] = foro['cutoffdate']
    
    

   

    return output



def epoch_to_dateCom(epoch):
    # Convertir epoch a hora local de Ecuador
    local_time = datetime.datetime.fromtimestamp(epoch, ecuador_tz)
    
    # Formatear usando Babel
    formatted_date = format_datetime(local_time, "EEEE d 'de' MMMM 'a las' hh:mma", locale='es')
    
    return formatted_date

# Función para ver las tareas en los próximos 7 días
def TareasProximas(diccionario, dias):
    # Obtener la fecha de hoy en Ecuador
    hoy = datetime.datetime.now(ecuador_tz).date()

    # Guardamos las tareas en un diccionario
    TareasProximos7Dias = {}
    MensajeFinal = "Estás serían las actividades más próximas 👀\n\n"
    MensajeFinal += f"\t》》*Actividades próximas* ({dias} Dias)🤓《《 \n\n"
    bandera = False
    
    for Materia in diccionario:
        Materia_esp = Materia.strip()
        for Tarea in diccionario[Materia]:
            
            # Convertir epoch a fecha en Ecuador y calcular la diferencia de días
            tarea_fecha = datetime.datetime.fromtimestamp(diccionario[Materia][Tarea], ecuador_tz).date()
            dias_para_tarea = (tarea_fecha - hoy).days
            
            # Si la tarea finaliza en los próximos 7 días, se añade al diccionario
            if dias_para_tarea <= dias and dias_para_tarea >= 0:
                bandera = True
                TareasProximos7Dias[Tarea] = diccionario[Materia][Tarea]
                
                MensajeFinal += f"  👀*`{Materia_esp}`* \n- _{Tarea}_ ➡️ _*{epoch_to_dateCom(diccionario[Materia][Tarea])}*_\n\n"
    
   

    if not bandera:
        MensajeFinal = f"No hay tareas para {dias} dias ?.\n"
    
    return MensajeFinal
