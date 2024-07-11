from Funciones_parcial import *

csv_cargado = False
while True: 
    opcion = input("1)carga un archivo csv\n2)Asignar likes, dislikes y followers aleatorios\n3)Imprime lista de influencers\n4)crea un archivo con los influencers mas famosos\n5)crea un archivo con los influencers mas infames\n6)saca un promedio de followers\n7)crea un archivo con los influencers ordenados en orden alfabetico\n8)Muestra al influencer mas famoso\n9)Salir\n")
    match opcion:
        case "1":
            influencers = cargar_un_csv(get_path_actual("posts.csv"))
            csv_cargado = True
        case "2":
            if csv_cargado == True:
                asignar_likes_aleatorios(influencers)
                asignar_dislikes_aleatorios(influencers)
                asignar_followers_aleatorios(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "3":    
            if csv_cargado == True:
                imprimir_influencers_lista(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "4":
            if csv_cargado == True:
                famosos(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "5":
            if csv_cargado == True:
                infames(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "6":
            if csv_cargado == True:
                prom_followers(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "7":
            if csv_cargado == True:
                influencer_alfabetico(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "8":
            if csv_cargado == True:
                likes_max(influencers)
            else:
                print("Primero debe cargar un CSV")
        case "9":
            break
        case _:
            print("Inserte una opcion correcta")