from data_stark import lista_personajes
from Funciones import *

while True:
    opcion = input("1)Listar Nombres\n2)Listar nombres y altura\n3)Altura maxima\n4)Altura minima\n5)Promedio altura\n6)Gordura maxima\n7)Gordura minima\n8)altura maxima heroe masculino\n9)altura maxima heroe femenino\n10)altura minima heroe masculino\n11)altura minima heroe femenino\n12)promedio altura heroe masculino\n13)promedio altura heroe femenino\n14)color de ojos\n15)color de pelo\n16)inteligencia\n17)heroes por color de ojos\n18)heroes por color de pelo\n19)heroes por inteligencia\n20)salir\n")
    match opcion:
        case "1":
            print_nombres(lista_personajes)
        case "2":
            print_nombres_y_alturas(lista_personajes)
        case "3":
            altura_maxima(lista_personajes)
        case "4":
            altura_minima(lista_personajes)
        case "5":
            promedio_altura(lista_personajes)
        case "6":
            gordura_maxima(lista_personajes)
        case "7":
            gordura_minima(lista_personajes)
        case "8":
            altura_maxima_heroe_masculino(lista_personajes)
        case "9":
            altura_maxima_heroe_femenino(lista_personajes)
        case "10":
            altura_minima_heroe_masculino(lista_personajes)
        case "11":
            altura_minima_heroe_femenino(lista_personajes)
        case "12":
            promedio_altura_heroe_masculino(lista_personajes)
        case "13":
            promedio_altura_heroe_femenino(lista_personajes)
        case "14":
            color_ojos(lista_personajes)
        case "15":
            color_pelo(lista_personajes)
        case "16":
            inteligencia(lista_personajes)
        case "17":
            heroes_por_color_ojos(lista_personajes)
        case "18":
            heroes_por_color_pelo(lista_personajes)
        case "19":
            heroes_por_inteligencia(lista_personajes)
        case "20":
            break
        case _:
            print("Opcion no valida")