import pygame

clock = pygame.time.Clock()
class Bala(pygame.sprite.Sprite):
    def __init__ (self, pos, imagenes, damage, velocidad, dick_vars):
        self.pos = pos
        self.imagenes = imagenes
        self.damage = damage
        self.velocidad = velocidad
        self.index = 0
        dick_vars["lista_balas"].append(self)
        self.imagenes_lista = []
        for i in range(12):
            image = pygame.image.load(f"{self.imagenes}/{i}.png")
            self.imagenes_lista.append(image)
        self.image = self.imagenes_lista[0]

    def dibujar_bala(self, superficie):
        superficie.blit(self.image, self.pos)

    def mover_bala(self, dick_vars:dict):
        self.pos[0] += self.velocidad
        if self.pos[0] > 800:
            self.borrar_bala(dick_vars["lista_balas"])
    
    def actualizar_animacion(self):
        if self.index < 11:
            self.index += 1
        else:
            self.index = 0
            
        self.image = self.imagenes_lista[self.index]
    
    def borrar_bala(self, lista_balas:dict):
        lista_balas.remove(self)