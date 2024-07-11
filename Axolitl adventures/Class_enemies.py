import pygame
from Class_bala_enemigo import Bala_enemigo

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
            case 2:
                self.vida = 2
                self.daño = 1
                self.velocidad = 3
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 2 hp.png")
            case 3:
                self.vida = 3
                self.daño = 2
                self.velocidad = 4
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 3 hp.png")
            case 4:
                self.vida = 1
                self.daño = 1
                self.velocidad = 0
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo que dispara.png")
            case 5:
                self.vida = 10
                self.daño = 1
                self.velocidad = 1
                self.image = pygame.image.load(f"{self.imagenes}/Enemigo 10 hp.png")

    
    def enemigo_mover(self):
        self.pos[0] -= self.velocidad
    
    def enemigo_shootear(self, dick_vars:dict):

        if self.cooldown == 0 and self.tipo == 4:
            self.cooldown = 60
            Bala_enemigo([self.pos[0] + self.rect.width - 3, self.pos[1]  + self.rect.height/2 - 6], "Axolitl adventures/Assets/Graficos/Armas", dick_vars)
        
    def bajar_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def borrar_enemigo(self, lista_enemigos:dict):
        lista_enemigos.remove(self)
    
    def chequear_colisiones(self, dick_vars:dict):
        if self.rect.collidelist(dick_vars["lista_balas_rect"]) != -1:
            self.bajar_vida(dick_vars, dick_vars["lista_balas"][self.rect.collidelist(dick_vars["lista_balas_rect"])].damage)
            dick_vars["lista_balas"][self.rect.collidelist(dick_vars["lista_balas_rect"])].borrar_bala(dick_vars["lista_balas"])
    
    def bajar_vida(self, dick_vars:dict, damage:int):
        if self.vida > 0:
            self.vida -= damage
        if self.vida <= 0:
            self.borrar_enemigo(dick_vars["lista_enemigos"])