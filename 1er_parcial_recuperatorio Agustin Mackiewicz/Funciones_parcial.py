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
        list: la lista influencers
    """
    if type(ruta_archivo) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(ruta_archivo) as archivo:
        lista_influencers = []
        for linea in archivo:
            influencer = {}
            caracteristicas = linea.split(",")
            influencer["id"] = caracteristicas[0]
            influencer["username"] = caracteristicas[1]
            influencer["likes"] = caracteristicas[2]
            influencer["dislikes"] = caracteristicas[3]
            influencer["followers"] = caracteristicas[4]
            if influencer["id"].isdigit():
                lista_influencers.append(influencer)
        print("el archivo se cargo con exito")
        return lista_influencers

def imprimir_influencers_lista (influencers:list):
    """Imprime la lista de influencers

    Args:
        influencers (list): es la lista de influencers
    """
    print("_____________________________________________________________")
    print("   ID   |    USERNAME   |   LIKES   |  DISLIKES  |  FOLLOWERS")
    for influencer in influencers:
        print(f"    {influencer['id']}   |    {influencer['username']}    |    {influencer['likes']}    |    {influencer['dislikes']}    |    {influencer['followers']}")
    print("_____________________________________________________________")
    
    
def asignar_likes_aleatorios (influencers:list):
    """Asigna una cantidad de likes aleatorio

    Args:
        influencers (list): es la lista de influencers
    """
    import random
    for influencer in influencers:
        influencer["likes"] = random.randint(500,3000)

def asignar_dislikes_aleatorios (influencers:list):
    """Asigna una cantidad de dislikes aleatorio

    Args:
        influencers (list): es la lista de influencers
    """
    import random
    for influencer in influencers:
        influencer["dislikes"] = random.randint(300,3500)

def asignar_followers_aleatorios (influencers:list):
    """Asigna una cantidad de followers aleatorio

    Args:
        influencers (list): es la lista de influencers
    """
    import random
    for influencer in influencers:
        influencer["followers"] = random.randint(10000,20000)


def famosos(influencers:list):
    """ Printea los datos de las personas que tienen mas de 2000 likes.

    Args:
        lista_influencers (list): es la lista de influencers
    """
    if type(influencers) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    primer_influencer = True
    for influencer in influencers:
            if float(influencer["likes"]) > 2000:
                if primer_influencer == True:
                    dik = [{"id":influencer["id"], "username":influencer["username"], "likes":influencer["likes"], "dislikes":influencer["dislikes"], "followers":influencer["followers"]}]
                    primer_influencer = False
                else:
                    dik.append({"id":influencer["id"], "username":influencer["username"], "likes":influencer["likes"], "dislikes":influencer["dislikes"], "followers":influencer["followers"]}) 
            ruta = get_path_actual ("Influencers_mas_likes.csv")
            with open(ruta, "w") as archivo:
                for participante in dik:
                    archivo.write(f"{participante["id"]},")
                    archivo.write(f"{participante["username"]},")
                    archivo.write(f"{participante["likes"]},")
                    archivo.write(f"{participante["dislikes"]},")
                    archivo.write(f"{participante["followers"]}\n")

def infames(influencers:list):
    """ Printea los datos de las personas que tienen mas dislikes que likes.

    Args:
        lista_influencers (list): es la lista de influencers
    """
    if type(influencers) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    primer_influencer = True
    for influencer in influencers:
            if float(influencer["likes"]) < float(influencer["dislikes"]):
                if primer_influencer == True:
                    dik = [{"id":influencer["id"], "username":influencer["username"], "likes":influencer["likes"], "dislikes":influencer["dislikes"], "followers":influencer["followers"]}]
                    primer_influencer = False
                else:
                    dik.append({"id":influencer["id"], "username":influencer["username"], "likes":influencer["likes"], "dislikes":influencer["dislikes"], "followers":influencer["followers"]}) 
            ruta = get_path_actual ("Influencers_con_mas_dislikes.csv")
            with open(ruta, "w") as archivo:
                for participante in dik:
                    archivo.write(f"{participante["id"]},")
                    archivo.write(f"{participante["username"]},")
                    archivo.write(f"{participante["likes"]},")
                    archivo.write(f"{participante["dislikes"]},")
                    archivo.write(f"{participante["followers"]}\n")


def prom_followers(lista_influencers:list):
    """saca el promedio de followers de los influencers
    Args:
        lista_influencers (list): es la lista de influencers
        tipo (str): es el tipo de bicicleta
    """
    suma = 0
    for participante in lista_influencers:
                suma += float(participante["followers"])
    promedio = suma / len(lista_influencers)
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
    
def influencer_alfabetico (influencers:list):
    """ordena las los influencers de forma alfabetica

    Args:
        influencer (list): lista de influencer
    """
    for i in range(len(influencers) - 1):
            for j in range(len(influencers) - i - 1):
                if influencers[j]["username"] > influencers[j + 1]["username"]:
                    auxiliar = influencers[j]
                    influencers[j] = influencers[j + 1]
                    influencers[j + 1] = auxiliar
    get_path_actual("Influencers_alfabetico.json")
    guardar_en_json("Influencers_alfabetico.json", influencers)

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

def likes_max(lista_influencers:list):
    """ Printea el nombre y los likes del influencer que tiene mayor cantidad de likes.

    Args:
        lista_influencers (list): es la lista de influencers
    """
    if type(lista_influencers) is not list:
        raise TypeError("La lista no es de tipo list")
    max = 0
    for influencer in lista_influencers:
            if float(influencer["likes"]) > max:
                max = float(influencer["likes"])
                influencer_likesmax = influencer
    print(influencer_likesmax["username"])
    print(influencer_likesmax["likes"])
