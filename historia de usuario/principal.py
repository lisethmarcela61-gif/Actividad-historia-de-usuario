from carro import Carro
from chofer import Chofer
from base_datos import Base_datos

bd = Base_datos()

while True:
    print ("1. Agregar nuevo carro")
    print ("2. Agregar chofer")
    print ("3. Mostrar carros")
    print ("4. Salir del sistema")

    op = input("Seleccion una opcion: ")

    if op == "1":
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        fecha_s = input("Fecha de salida: ")
        fecha_l = input("Fecha limite de entrega: ")
        b = Carro(placa,modelo,color,fecha_s,fecha_l)
        bd.guardar_carros(b)

    if op == "2":
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        licencia = input("El chofer tiene licencia si/no: ")
        n = Chofer(nombre,documento,licencia)
        bd.guardar_chofer(n)

    if op == "3":
        bd.ver_datos()
    
    if op == "4":
        break
        
