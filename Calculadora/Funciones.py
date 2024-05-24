def pedir_numero(mensaje) -> int:
    valor = input(mensaje)
    if valor.isdigit() == True:
        valor = int(valor)
    else:
        print("Ingrese un numero valido")
    return valor

def sumar(primer_operando, segundo_operando) -> int:
    suma = primer_operando + segundo_operando
    return suma

def restar(primer_operando, segundo_operando) -> int:
    resta = primer_operando - segundo_operando
    return resta

def multiplicar(primer_operando, segundo_operando) -> int:
    multiplicacion = primer_operando * segundo_operando
    return multiplicacion

def dividir(primer_operando, segundo_operando) -> int:
    division = primer_operando / segundo_operando
    return division

def factorializacion(operando) -> int:
    factorial = 0
    for i in range(0, operando):
        if i == 1 or i == 0:
            factorial = 1
        else:
            factorial *= i
    return factorial