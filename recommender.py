import sys
import time

print("Escribe los datos que estés buscando en tu vivienda. Si hay alguno que no quieras fijar, escribe un guión (-) y pulsa [ENTER]")
print("Pulsa [ENTER] para continuar")
price = input('Precio máximo (escríbelo sin puntos ni comas): ')
rooms = input('Número de habitaciones: ')
bathrooms = input('Número de baños: ')
print(" ")
print('Inserta uno de estos valores en función del tipo de casa que busques.')
print('Chalet')
print('Piso')
print('Adosado')
print('Dúplex')
print('Ático')
homeType = input('Tipo de casa: ')
print(" ")
print('A continuación, escribe "sí" si lo necesitas y escribe "-" si no es un requisito en la vivienda')
elevator = input('Ascensor: ')
storage_room = input('Trastero: ')
parking = input('Parking: ')
pool = input('Piscina: ')
terraze = input('Terraza: ')
print(" ")
print('Escribe el distrito en el que estés buscando vivienda. Las posiblildades son:')
print('Centro')
print('Arganzuela')
print('Retiro')
print('Salamanca')
print('Chamberí')
location = input('Ubicación: ')

print(" ")
time.sleep(2)
print('Procesando...')

if price == '-' or price == "":
    print('entra por aqui')





# print("Escribe los datos que estés buscando en tu vivienda. Si hay alguno que no quieras fijar, pulsa [ENTER]")
# print("Pulsa [ENTER] para continuar")
# print "Precio máximo:" + sys.argv[0]
# print "Número de habitaciones:" + sys.argv[1]
# print "Número de baños:" + sys.argv[1]
# print "Tipo de casa (chalet, apartamento, adosado, dúplex o ático):" + sys.argv[2]
# print "Necesario ejecutar con al menos dos parámetros"
# print "python programa.py param1 param2"