# Librería para manejo de fecha y hora en python
from datetime import datetime, date, time, timedelta
import locale

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

# Mostrar la fecha y la hora actual del sistema
date_and_time = datetime.now()
print(date_and_time)

# Mostrar sólo el día actual
print(f'Día actual: {date_and_time.day}')
print(f'Mes actual: {date_and_time.month}')
print(f'Año actual: {date_and_time.year}')
print(
    f'Fecha actual: {date_and_time.day}/{date_and_time.month}/{date_and_time.year}')
print(f'Hora actual: {date_and_time.hour}')
print(f'Minuto actual: {date_and_time.minute}')
print(f'Segundo actual: {date_and_time.second}')

# Crear objetos de tipo hora/fecha
hora1 = time(7, 1, 0)
print(hora1)
hora2 = time(10, 5, 8)
print(hora2)
if hora1 > hora2:
    print('La primera hora es mayor')
else:
    print('La segunda hora es mayor')

# # Obtener sólo la fecha actual
fecha = date.today()
print(fecha)
fecha2 = date(2020, 4, 8)
print(fecha2)
if fecha > fecha2:
    print('La primera fecha es mayor')
else:
    print('La segunda fecha es mayor')

# # Agregar días/semanas a una fecha
nueva_fecha = fecha + timedelta(weeks=52, days=20)
print(nueva_fecha)

# # Formatos de fechas/horas
print(fecha.strftime('%d-%m-%Y Días transcurridos: %j, Semanas transcurridas: %W'))
print(fecha.strftime('%A, %d de %B de %Y'))
print(date_and_time.strftime('%I:%M:%S %p'))
