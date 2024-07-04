import json

def print_nombres(lista_heroes:list):
    """ Printea el nombre de todos los heroes

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    for heroe in lista_heroes:
        print(heroe["nombre"])
    


def print_nombres_y_alturas(lista_heroes:list):
    """ Printea el nombre y la altura de todos los heroes

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    for heroe in lista_heroes:
        print(heroe["nombre"], heroe["altura"])



def altura_maxima(lista_heroes:list):
    """ Printea el nombre del heroe que tiene la altura maxima.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    max = 0
    for heroe in lista_heroes:
            if float(heroe["altura"]) > max:
                max = float(heroe["altura"])
                heroe_alturamax = heroe
    print(heroe_alturamax["nombre"])

    

def altura_minima(lista_heroes:list):
    """ Printea el nombre del heroe que tiene la altura minima.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    min = True
    minimo = 0
    for heroe in lista_heroes:
            if float(heroe["altura"]) < minimo or min == True:
                minimo = float(heroe["altura"])
                heroe_alturamin = heroe
                min = False
    print(heroe_alturamin["nombre"])

    

def promedio_altura(lista_heroes:list):
    """ Printea el promedio de altura de todos los heroes

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    suma = 0
    for heroe in lista_heroes:
        suma += float(heroe["altura"])
    promedio = suma / len(lista_heroes)
    print(promedio)

    
def gordura_maxima(lista_heroes:list):
    """ Printea el nombre del heroe que tiene el major peso.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    max = 0
    for heroe in lista_heroes:
            if float(heroe["peso"]) > max:
                max = float(heroe["peso"])
                heroe_gorduramax = heroe
    print(heroe_gorduramax["nombre"])



def gordura_minima(lista_heroes:list):
    """ Printea el nombre del heroe que tiene el menor peso.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    min = True
    minimo = 0
    for heroe in lista_heroes:
            if float(heroe["peso"]) < minimo or min == True:
                minimo = float(heroe["peso"])
                heroe_gorduramin = heroe
                min = False
    print(heroe_gorduramin["nombre"])

    

def nombres_heroes_femenino(lista_heroes:list):
    """ Printea los nombres de todos los heroes femeninos
    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    for heroe in lista_heroes:
        if heroe["genero"] == "F":
            print(heroe["nombre"])

    

def nombres_heroes_masculino(lista_heroes:list):
    """ Printea los nombres de todos los heroes masculinos
    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            print(heroe["nombre"])

    

def altura_maxima_heroe_masculino(lista_heroes:list):
    """ Printea el nombre del heroe masculino que tiene la mayor altura.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    max = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "M" and float(heroe["altura"]) > max:
            max = float(heroe["altura"])
            heroe_alturamax = heroe
    print(heroe_alturamax["nombre"])

    

def altura_maxima_heroe_femenino(lista_heroes:list):
    """ Printea el nombre del heroe femenino que tiene la mayor altura.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    max = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "F" and float(heroe["altura"]) > max:
            max = float(heroe["altura"])
            heroe_alturamax = heroe
    print(heroe_alturamax["nombre"])

    

def altura_minima_heroe_masculino(lista_heroes:list):
    """ Printea el nombre del heroe masculino que tiene la menor altura.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    min = True
    minimo = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "M" and float(heroe["altura"]) < minimo or min == True:
            minimo = float(heroe["altura"])
            heroe_alturamin = heroe
            min = False
    print(heroe_alturamin["nombre"])
    
    

def altura_minima_heroe_femenino(lista_heroes:list):
    """ Printea el nombre del heroe femenino que tiene la menor altura.

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    min = True
    minimo = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "F" and float(heroe["altura"]) < minimo or min == True:
            minimo = float(heroe["altura"])
            heroe_alturamin = heroe
            min = False
    print(heroe_alturamin["nombre"])

    """ Printea el nombre del heroe femenino que tiene la menor altura.
    """ 

def promedio_altura_heroe_masculino(lista_heroes:list):
    """ Printea el promedio de altura de todos los heroes masculinos

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    suma = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "M":
            suma += float(heroe["altura"])
    promedio = suma / len(lista_heroes)
    print(promedio) 

    

def promedio_altura_heroe_femenino(lista_heroes:list):
    """ Printea el promedio de altura de todos los heroes femeninos

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    suma = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "F":
            suma += float(heroe["altura"])
    promedio = suma / len(lista_heroes)
    print(promedio)

    

def color_ojos(lista_heroes:list):
    """ Printea la cantidad de heroes segun su color de ojos

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        color = heroe["color_ojos"]
        if color not in dik:
            dik[color] = 1
        else:
            dik[color]+= 1 
    for color in dik:
        print(color, dik[color])

    """ Printea el color de ojos de todos los heroes
    """

def color_pelo(lista_heroes:list):
    """ Printea la cantidad de heroes segun su color de pelo

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        color = heroe["color_pelo"]
        if color not in dik:
            dik[color] = 1
        else:
            dik[color]+= 1 
    for color in dik:
        print(color, dik[color])

    

def inteligencia(lista_heroes:list):
    """ Printea la cantidad de heroes segun su inteligencia

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        valor = heroe["inteligencia"]
        if valor == "":
            dik["no lo tiene"] = 1
        elif valor not in dik:
            dik[valor] = 1
        else:
            dik[valor]+= 1 
    for valor in dik:
        print(valor, dik[valor])

    

def heroes_por_color_ojos(lista_heroes:list):
    """Printea todos los heroes por color de ojos

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        color = heroe["color_ojos"]
        if color not in dik:
            dik[color] = [heroe["nombre"]]
        else:
            dik[color].append(heroe["nombre"])
    for color in dik:
        print(color)
        for heroe in dik[color]:
            print(heroe)

    

def heroes_por_color_pelo(lista_heroes:list):
    """Printea todos los heroes por color de pelo

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        color = heroe["color_pelo"]
        if color not in dik:
            dik[color] = [heroe["nombre"]]
        else:
            dik[color].append(heroe["nombre"])
    for color in dik:
        print(color)
        for heroe in dik[color]:
            print(heroe)

    

def heroes_por_inteligencia(lista_heroes: list):
    """Nombre de los heroes por la inteligencia que tienen

    Args:
        lista_heroes (list): es la lista de heroes
    """    
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        valor = heroe["inteligencia"]
        if valor == "":
            dik["no lo tiene"] = [heroe["nombre"]]
        elif valor not in dik:
            dik[valor] = [heroe["nombre"]]
        else:
            dik[valor].append(heroe["nombre"])
    for valor in dik:
        print(valor)
        for heroe in dik[valor]:
            print(heroe)
    
def guardar_en_csv(ruta:str, lista_heroes:list):
    """Guarda la lista de heroes en un archivo csv

    Args:
        ruta (str): Ruta donde se guardaran los datos
        lista_heroes (list): La lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    if type(ruta) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(ruta, "w") as archivo:
        for heroe in lista_heroes:
            archivo.write(heroe["nombre"] + ",")
            archivo.write(heroe["genero"] + ",")
            archivo.write(heroe["altura"] + ",")
            archivo.write(heroe["peso"] + ",")
            archivo.write(heroe["color_ojos"] + ",")
            archivo.write(heroe["color_pelo"] + ",")
            archivo.write(heroe["fuerza"] + ",")
            archivo.write(heroe["inteligencia"] + "\n")

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
        list: la lista de heroes
    """
    if type(ruta_archivo) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(ruta_archivo) as archivo:
        lista_heroes = []
        for linea in archivo:
            heroe = {}
            caracteristicas = linea.split(",")
            heroe["nombre"] = caracteristicas[0]
            heroe["genero"] = caracteristicas[1]
            heroe["altura"] = caracteristicas[2]
            heroe["peso"] = caracteristicas[3]
            heroe["color_ojos"] = caracteristicas[4]
            heroe["color_pelo"] = caracteristicas[5]
            heroe["fuerza"] = caracteristicas[6]
            heroe["inteligencia"] = caracteristicas[7]
            lista_heroes.append(heroe)

    return lista_heroes

def cargar_un_json(ruta_archivo:str)->dict:
    """carga un archivo json

    Args:
        ruta_archivo (str): Es la ruta del archivo

    Returns:
        dict: Contenido del archivo json
    """
    if type(ruta_archivo) is not str:
        raise TypeError("La ruta no es de tipo str")
    with open(ruta_archivo) as archivo:
        lista_heroes = json.load(archivo)
    return lista_heroes

def guardar_en_json(ruta:str, lista_heroes:list):
    """Guarda la lista en un archivo json

    Args:
        ruta (str): Ruta donde se guardaran los datos
        lista_heroes (list): La lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    if type(ruta) is not str:
        raise TypeError("La ruta no es de tipo str")
    variable_que_se_te_pinte = {"heroes":lista_heroes}
    with open(ruta, "w") as archivo:
        json.dump(variable_que_se_te_pinte, archivo, indent=4)

def heroes_por_color_pelo_usuario(lista_heroes:list):
    """Printea todos los heroes por color de pelo segun eleccion del usuario

    Args:
        lista_heroes (list): es la lista de heroes
    """
    if type(lista_heroes) is not list:
        raise TypeError("La lista no es de tipo list")
    dik = {}
    for heroe in lista_heroes:
        color = heroe["color_pelo"]
        if color not in dik:
            dik[color] = [heroe["nombre"]]
        else:
            dik[color].append(heroe["nombre"])
    print("elige un color")
    for color in dik.keys():
        print(color)
    color = input()
    if color not in dik.keys():
        print("color no valido")
        return None
    for heroe in dik[color]:
        print(heroe)

def swap_lista(alumno: list, i: int, j: int):
    """swap de dos elementos

    Args:
        alumno (list): lista de alumnos
        i (int): el primer indice
        j (int): el segundo indice
    """
    aux = alumno[i]
    alumno[i] = alumno[j]
    alumno[j] = aux

def ordenar_empleados_doble_criterio_ascendente(alumnos: list, campo1, campo2, campo3):
    tam= len(alumnos)
    for i in range(0, tam-1):
      for j in range(i +1, tam):
        if alumnos[i][campo1] == alumnos[j][campo1]:
            if alumnos[i][campo2] == alumnos[j][campo2]:
                if alumnos[i][campo3] > alumnos[j][campo3]:
                    swap_lista(alumnos, i, j)
                elif alumnos[i][campo2] > alumnos[j][campo2]:
                    swap_lista(alumnos, i, j)
        elif alumnos[i][campo1] > alumnos[j][campo1]:
            swap_lista(alumnos, i, j)