from Funciones_parcial import *

csv_cargado = False
while True: 
    opcion = input("1)Cargar un CSV\n2)Asignar tiempo aleatorio a los participantes\n3)Imprimir lista de participantes\n4)Determinar el ganador\n5)Guardar una lista de participantes segun su tipo de bicicleta\n6)Promedio de tiempo por tipo\n7)Ordenar bicicletas segun tiempo\n8)Guardar en JSON\n9)Salir\n")
    match opcion:
        case "1":
            participantes = cargar_un_csv(get_path_actual("bicicletas.csv"))
            csv_cargado = True
        case "2":
            if csv_cargado == True:
                asignar_tiempo_aleatorio(participantes)
            else:
                print("Primero debe cargar un CSV")
        case "3":
            if csv_cargado == True:
                imprimir_participantes_lista(participantes)
            else:
                print("Primero debe cargar un CSV")
        case "4":
            if csv_cargado == True:
                ganador(participantes)
            else:
                print("Primero debe cargar un CSV")
        case "5":
            if csv_cargado == True:
                participante_por_bicicleta(participantes)
            else:
                print("Primero debe cargar un CSV")
        case "6":
            if csv_cargado == True:
                prom_tiempo_tipo(participantes, "BMX")
                prom_tiempo_tipo(participantes, "MTB")
                prom_tiempo_tipo(participantes, "PLAYERA")
                prom_tiempo_tipo(participantes, "PASEO")
            else:
                print("Primero debe cargar un CSV")
        case "7":
            if csv_cargado == True:
                lista_ordenada = ordenar_bicicletas_ascendente(participantes)
                bici_ordenada_tipo(participantes)
            else:
                print("Primero debe cargar un CSV")
        case "8":
            if csv_cargado == True:
                guardar_en_json(get_path_actual("bicicletas_ordenadas.json"), lista_ordenada)
            else:
                print("Primero debe cargar un CSV")
        case "9":
            break