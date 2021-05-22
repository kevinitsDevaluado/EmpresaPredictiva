#Fechas y Horas
from datetime import datetime

def get_fecha_hora():
    #fecha actual
    now = datetime.now()
    dia = now.day
    mes = now.month
    anio = now.year
    fecha = str(mes)+'/'+str(dia)+'/'+str(anio)
        
    aux_mes = ''
        
    #verificacion de mes -> str_mes
    if mes == 1:
        aux_mes = 'Enero'
    if mes == 2:
        aux_mes = 'Febrero'
    if mes == 3:
        aux_mes = 'Marzo'
    if mes == 4:
        aux_mes = 'Abril'
    if mes == 5:
        aux_mes = 'Mayo'
    if mes == 6:
        aux_mes = 'Junio'
    if mes == 7:
        aux_mes = 'Julio'
    if mes == 8:
        aux_mes = 'Agosto'
    if mes == 9:
        aux_mes = 'Septiembre'
    if mes == 10:
        aux_mes = 'Octubre'
    if mes == 11:
        aux_mes = 'Noviembre'
    if mes == 12:
        aux_mes = 'Diciembre'
              
    #Fecha Actual
    fecha_actual = str(dia) + ' de ' + str(aux_mes) + ' de ' + str(anio)
        
    #Hora actual
    x = datetime.now()
    hora_actual = str(x.hour)+':'+str(x.minute)+':'+str(x.second)
        
    ahora = fecha_actual + ' - ' + hora_actual
    
    return ahora