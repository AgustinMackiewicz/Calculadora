import pygame
import random

class Powerups:
    def __init__(self, pos, imagen, dick_vars:dict):
        self.imagenes = imagen
        self.pos = pos
        self.index = 0
        self.velocidad = 10
        dick_vars["lista_powerups"].append(self)
        
        i = random.randint(1, 7)
        self.image = pygame.image.load(f"{self.imagenes}/Amongus{i}.png")
    
    def mover_powerup(self, dick_vars:dict):
        self.pos[0] -= self.velocidad
        if self.pos[0] < 0:
            self.borrar_powerups(dick_vars["lista_powerups"])

    def dibujar_powerup(self, superficie):
        superficie.blit(self.image, self.pos)
        
    def borrar_powerups(self, lista_powerups:dict):
        lista_powerups.remove(self)