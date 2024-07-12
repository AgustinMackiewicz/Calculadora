import pygame
from Class_bala_enemigo import Bala_enemigo
import random
from Class_powerups import Powerups

class Enemigo:

    def __init__(self, pos, imagenes, tipo, dick_vars):

        self.pos = pos
        self.imagenes = imagenes
        self.tipo = tipo
        self.dick_vars = dick_vars
        dick_vars["lista_enemigos"].append(self)
        Enemigo.determinar_estadisticas(self)
        self.rect = self.image.get_rect()
        self.cooldown = 0

    
    def dibujar(self, superficie):
        superficie.blit(self.image, (self.pos[0], self.pos[1]))

    def determinar_estadisticas(self):
        match self.tipo:
            case 1:
                self.vida = 1
                self.daño = 1
                self.velocidad = 2
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 1 hp.png")
                self.score = 100
            case 2:
                self.vida = 2
                self.daño = 1
                self.velocidad = 3
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 2 hp.png")
                self.score = 200
            case 3:
                self.vida = 3
                self.daño = 2
                self.velocidad = 4
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 3 hp.png")
                self.score = 300
            case 4:
                self.vida = 1
                self.daño = 1
                self.velocidad = 0
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo que dispara.png")
                self.score = 100
            case 5:
                self.vida = 10
                self.daño = 1
                self.velocidad = 0
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 10 hp.png")
                self.score = 1000

    
    def enemigo_mover(self):
        self.pos[0] -= self.velocidad
        if self.pos[0] < 0:
            self.pos[0] = 1001
    
    def enemigo_shootear(self, dick_vars:dict):

        if self.cooldown == 0 and self.tipo == 4:
            self.cooldown = 90
            Bala_enemigo([self.pos[0] + self.rect.width - 3, self.pos[1]  + self.rect.height/2 - 6], dick_vars["bala_enemigo_img"], dick_vars)
        
    def bajar_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def borrar_enemigo(self, lista_enemigos:dict, dick_vars:dict):
        aleatorio = random.randint(0, 100)
        if aleatorio < 5:
            Powerups([self.pos[0] + self.rect.width - 3, self.pos[1]  + self.rect.height/2 - 6], dick_vars["powerup_img"], dick_vars)
        dick_vars["score"] += self.score
        lista_enemigos.remove(self)
    
    def chequear_colisiones(self, dick_vars:dict):
        try:
            if self.rect.collidelist(dick_vars["lista_balas_rect"]) != -1:
                self.bajar_vida(dick_vars, dick_vars["lista_balas"][self.rect.collidelist(dick_vars["lista_balas_rect"])].damage)
                dick_vars["lista_balas"][self.rect.collidelist(dick_vars["lista_balas_rect"])].borrar_bala(dick_vars["lista_balas"])
        except:
            pass
    def bajar_vida(self, dick_vars:dict, damage:int):
        if self.vida > 0:
            self.vida -= damage
        if self.vida <= 0:
            self.borrar_enemigo(dick_vars["lista_enemigos"], dick_vars)
    
    def posicionar_enemigo(lista_enemigos:list, columna:int):
        while len(lista_enemigos) < 8:
            lista_enemigos.append(-1)
        lista_spawns = []
        for i in range(len(lista_enemigos)):
            aleatorio = random.randint(0, len(lista_enemigos) - 1)
            Enemigo = lista_enemigos.pop(aleatorio)
            lista_spawns.append(Enemigo)
        for enemigo in range(len(lista_spawns)):
            if lista_spawns[enemigo] != -1:
                match columna:
                    case 1:
                        lista_spawns[enemigo].pos = [720, 50 + (enemigo * 60)]
                    case 2:
                        lista_spawns[enemigo].pos = [560, 50 + (enemigo * 60)]

    def crear_lista_enemigos (cantidad_enemigos:int, enemigos_permitidos:list, dick_vars:dict):
        columna_1 = []
        columna_2 = []
        for i in range(cantidad_enemigos):
            aleatorio = random.randint(0, len(enemigos_permitidos) - 1)
            enemigo = enemigos_permitidos[aleatorio]
            match enemigo:
                case 1 | 2 | 3:
                    numero = random.randint(0, 1)
                    if numero == 0:
                        columna_1.append(Enemigo([2000, 0], dick_vars["enemigo_img"], enemigo, dick_vars))
                    else:
                        columna_2.append(Enemigo([2000, 0], dick_vars["enemigo_img"], enemigo, dick_vars))
                case 4:
                    columna_1.append(Enemigo([2000, 0], dick_vars["enemigo_img"], enemigo, dick_vars))
                case 5:
                    columna_2.append(Enemigo([2000, 0], dick_vars["enemigo_img"], enemigo, dick_vars))
        Enemigo.posicionar_enemigo(columna_1, 1)
        Enemigo.posicionar_enemigo(columna_2, 2)       

    def generar_wave(dick_vars:dict):
        if dick_vars["waves"] < 5:
            Enemigo.crear_lista_enemigos(4, [1, 4], dick_vars)
        elif dick_vars["waves"] < 10:
            Enemigo.crear_lista_enemigos(6, [1, 4, 5], dick_vars)
        elif dick_vars["waves"] < 15:
            Enemigo.crear_lista_enemigos(6, [2, 4, 5], dick_vars)
        else:
            Enemigo.crear_lista_enemigos(8, [3, 4, 5], dick_vars)
        dick_vars["waves"] += 1
        