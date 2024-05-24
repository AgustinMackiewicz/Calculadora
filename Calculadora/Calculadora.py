from Funciones import *

valor_a = None
valor_b = None

while True:
    opcion = input("1)ingresa operando A\n2)Ingresa operando B\n3)Calcular suma de A y B\n4)Calcular resta de A y B\n5)Calcular multiplicacion de A y B\n6)Calcular division de A y B\n7)Calcular factorial de A y B\n8)Salir\n")
    match opcion:
        case "1":
            if valor_a == None:
                valor_a = pedir_numero("Ingrese el valor del operando A\n")
            else:
                print("Numero ya ingresado")
        case "2":
            if valor_b == None:
                valor_b = pedir_numero("Ingrese el valor del operando B\n")
            else:
                print("Numero ya ingresado")
        case "3":
            if valor_a != None and valor_b != None:
                suma = sumar(valor_a, valor_b)
                print(f"el resultado de la suma de {valor_a} y de {valor_b} es {suma}")
            else:
                print ("ingrese los valores de A y B primero")
        case "4":
            if valor_a != None and valor_b != None:
                resta = restar(valor_a, valor_b)
                print(f"el resultado de la resta de {valor_a} y de {valor_b} es {resta}")
            else:
                print ("ingrese los valores de A y B primero")
        case "5":
            if valor_a != None and valor_b != None:
                multiplicacion = multiplicar(valor_a, valor_b)
                print(f"el resultado de la multiplicacion de {valor_a} y de {valor_b} es {multiplicacion}")
            else:
                print ("ingrese los valores de A y B primero")
        case "6":
            if valor_a != None and valor_b != None:
                division = dividir(valor_a, valor_b)
                print(f"el resultado de la division de {valor_a} y de {valor_b} es {division}")
            else:
                print ("ingrese los valores de A y B primero")
        case "7":
            if (valor_a != None and valor_a > 0) and (valor_b != None and valor_b > 0):
                resultado_a = factorializacion(valor_a)
                resultado_b = factorializacion(valor_b)
                print(f"el factorial de {valor_a} es {resultado_a} y el resultado del factorial de {valor_b} es {resultado_b}")
            else:
                print ("ingrese un valor valido a, A y B primero")
        case "8":
            break
        case _:
            print("Inserte una opcion correcta")
