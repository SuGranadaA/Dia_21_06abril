#Importamos la librería
import calendar

#Identificamos el año
año = int(input("Ingrese un año para imprimir su calendario: "))

#Imprimimos el calendario de dos maneras distintas, una pudiendo acomodar como se ve, y a otra, muy estándar
calendar.prcal(año, w=0, l=1, c=3, m=2)
print("\nO también de esta manera: ")
calendar.prcal(año)

#Imprimimos Septiembre de tal año
print("\nVemos Septiembre de", año, "\n")
calendar.prmonth(año, 9)

#Septiembre desde el jueves
print("\nVemos Octubre de", año, "\n")
jueves = calendar.TextCalendar(firstweekday=3)
oct_jueves = jueves.formatmonth(año, 10)
print(oct_jueves)

#Creamos el ciclo para el iterador del sistema
print("\nNúmero con el que se identifica cada día, comenzando por el Lunes\n")
iter1 = calendar.Calendar()
for i in iter1.iterweekdays():
    print(i, end=" ")
print(" ")

#Creamos el ciclo para nuestro propio iterador
print(
    "\nNúmero con el que se identifica cada día, comenzando por el Domingo\n")
iter2 = calendar.Calendar(firstweekday=6)
for i in iter2.iterweekdays():
    print(i, end=" ")
print(" ")

#Imprimimos una lista de las semanas en un mes
print("\nLas semanas completas del mes de Noviembre del año", año, "\n")
mes = calendar.Calendar()
print(mes.monthdatescalendar(año, 11))

#Imprimimos los días de las semanas de el mes anterior
print("\nDías contenidos en el ejercicio anterior\n")
itermes = calendar.Calendar()
for i in itermes.itermonthdates(año, 11):
    print(i, end="  ,  ")
