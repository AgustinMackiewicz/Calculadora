import json

def get_path_actual(nombre_archivo:str)->str:
    """Devuelve el directorio actual

    Args:
        nombre_archivo (str): el nombre del archivo

    Returns:
        str: el directorio actual
    """
    if type(nombre_archivo) is not str:
        raise TypeError("El nombre del archivo no es de tipo str")
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def cargar_un_csv(ruta_archivo:str)->list:
    """carga un archivo csv

    Args:
        ruta_archivo (str): la ruta del archivo

    Returns:
        list: la lista participantes
    """
    if type(ruta_archivo) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(ruta_archivo) as archivo:
        lista_participantes = []
        for linea in archivo:
            participante = {}
            caracteristicas = linea.split(",")
            participante["id_bike"] = caracteristicas[0]
            participante["nombre_del_dueño"] = caracteristicas[1]
            participante["tipo"] = caracteristicas[2]
            participante["tiempo"] = caracteristicas[3]
            if participante["id_bike"].isdigit():
                lista_participantes.append(participante)
        return lista_participantes

def imprimir_participantes_lista (participantes:list):
    """Imprime la lista de participantes

    Args:
        participantes (list): es la lista de participantes
    """
    print("_____________________________________________________________")
    for participante in participantes:
        print(f"    {participante['id_bike']}    |    {participante['nombre_del_dueño']}    |    {participante['tipo']}    |    {participante['tiempo']}")
    print("_____________________________________________________________")
    
    
def asignar_tiempo_aleatorio (participantes:list):
    """Asigna un tiempo aleatorio

    Args:
        participantes (list): es la lista de participantes
    """
    import random
    for participante in participantes:
        participante["tiempo"] = random.randint(50,120)

def ganador(participantes:list):
    """ Printea el nombre y el tiempo de la persona que tiene el menor tiempo.

    Args:
        lista_participantes (list): es la lista de heroes
    """
    if type(participantes) is not list:
        raise TypeError("La lista no es de tipo list")
    min = True
    ganador = []
    minimo = 0
    for participante in participantes:
            if float(participante["tiempo"]) < minimo or min == True:
                ganador.clear()
                minimo = float(participante["tiempo"])
                ganador.append(participante)
                min = False
            elif float(participante["tiempo"]) == minimo:
                ganador.append(participante)
    if len(ganador) == 1:
        print("ganador")
        print(ganador[0]["nombre_del_dueño"])
        print(ganador[0]["tiempo"])
    else:
        print("empate")
        for participante in ganador:
            print(participante["nombre_del_dueño"])
            print(participante["tiempo"])
def participante_por_bicicleta(lista_participantes:list):
    #No Funciona
    """Printea todos los participantes por bicicleta que tienen

    Args:
        lista_participantes (list): es la lista de participantes
    """
    if type(lista_participantes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    
    for participante in lista_participantes:
        bicicleta = participante["tipo"]
        if bicicleta not in dik:
            dik[bicicleta] = [{"nombre_del_dueño":participante["nombre_del_dueño"], "tipo":participante["tipo"], "id_bike":participante["id_bike"], "tiempo":participante["tiempo"]}]
            
        else:
            dik[bicicleta].append({"nombre_del_dueño":participante["nombre_del_dueño"], "tipo":participante["tipo"], "id_bike":participante["id_bike"], "tiempo":participante["tiempo"]}) 
    print("elige un bicicleta")
    for bicicleta in dik.keys():
        print(bicicleta)
    bicicleta = input()
    ruta = get_path_actual(f"{bicicleta}.csv")
    if bicicleta not in dik.keys():
        print("bicicleta no valido")
        return None
    with open(ruta, "w") as archivo:
        for participante in dik[bicicleta]:
                archivo.write(f"{participante["nombre_del_dueño"]},")
                archivo.write(f"{participante["tipo"]},")
                archivo.write(f"{participante["tiempo"]},")
                archivo.write(f"{participante["id_bike"]}\n")


def prom_tiempo_tipo(lista_participantes:list, tipo:str):
    """saca el promedio de tiempo de las bicicletas

    Args:
        lista_participantes (list): es la lista de participantes
        tipo (str): es el tipo de bicicleta
    """
    suma = 0
    for participante in lista_participantes:
        if participante["tipo"] == tipo:
                suma += float(participante["tiempo"])
    promedio = suma / len(lista_participantes)
    print(promedio)

def swap_lista(participantes: list, i: int, j: int):
    """swap de dos elementos

    Args:
        participantes (list): lista de participantess
        i (int): el primer indice
        j (int): el segundo indice
    """
    aux = participantes[i]
    participantes[i] = participantes[j]
    participantes[j] = aux
    
def bici_ordenada_tipo (participantes:list):
     for i in range(0, len(participantes)-1):
        for j in range(i +1, len(participantes)):
                if float(participantes[i]["tiempo"]) > float(participantes[j]["tiempo"]):
                    swap_lista(participantes, i, j)


def ordenar_bicicletas_ascendente (lista_participantes:list):
    dik = {}
    for participante in lista_participantes:
        bicicleta = participante["tipo"]
        if bicicleta not in dik:
            dik[bicicleta] = [{"nombre_del_dueño":participante["nombre_del_dueño"], "tipo":participante["tipo"], "id_bike":participante["id_bike"], "tiempo":participante["tiempo"]}]
            
        else:
            dik[bicicleta].append({"nombre_del_dueño":participante["nombre_del_dueño"], "tipo":participante["tipo"], "id_bike":participante["id_bike"], "tiempo":participante["tiempo"]})
    lista_estoy_listo = []
    for tipo in dik.keys():
        bici_ordenada_tipo(dik[tipo])
        for participante in dik[tipo]:
            lista_estoy_listo.append(participante)
    for participante in lista_estoy_listo:
        print(f"{participante["nombre_del_dueño"]}, {participante['tiempo']}, {participante['id_bike']}, {participante['tipo']}")
    return lista_estoy_listo

def guardar_en_json(ruta:str, lista_bicicleta:list):
    """Guarda la lista en un archivo json

    Args:
        ruta (str): Ruta donde se guardaran los datos
        lista_bicicleta (list): La lista de bicicleta
    """
    if type(lista_bicicleta) is not list:
        raise TypeError("La lista no es de tipo list")
    if type(ruta) is not str:
        raise TypeError("La ruta no es de tipo str")
    variable_que_se_te_pinte = {"bicicleta":lista_bicicleta}
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(variable_que_se_te_pinte, archivo, indent=4)