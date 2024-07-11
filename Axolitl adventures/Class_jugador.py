import pygame
from Class_bala import Bala

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("Axolitl adventures/Assets/Graficos/Ajolote.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vida = 3
        self.cooldown = 0
        
    

    def mover(self, direccion):
        match direccion:
            case "arriba":
                self.y -= 8
                if self.y < 0:
                    self.y = 0
            case "abajo":
                self.y += 8
                if self.y > 600 - self.rect.height:
                    self.y = 600 - self.rect.height
            case "izquierda":
                self.x -= 8
                if self.x < 0:
                    self.x = 0
            case "derecha":
                self.x += 8
                if self.x > 300 - self.rect.width:
                    self.x = 300 - self.rect.width

    def dibujar(self, superficie):
        superficie.blit(self.image, (self.x, self.y))
    
    def shootear_bala(self, dick_vars:dict):
        power_ups_obtenidos = dick_vars["power_ups"]
        if self.cooldown == 0:
            dick_vars["disparo"].play()
            self.cooldown = 30
            match power_ups_obtenidos:
                case 0:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 6], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                case 1:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                case 2:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 10, dick_vars)
                case 3:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                case 4:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                case 5:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 12, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                case 6:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 2, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 1, 10, dick_vars)
                case 7:
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 5, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 12], "Axolitl adventures/Assets/Graficos/Nokia 1100", 5, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 + 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 3, 15, dick_vars)
                    Bala([self.x + self.rect.width - 3, self.y  + self.rect.height/2 - 24], "Axolitl adventures/Assets/Graficos/Nokia 1100", 3, 15, dick_vars)

    
    def bajar_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
    def bajar_vida(self, dick_vars:dict):
        if self.vida > 0:
            self.vida -= 1
        if self.vida == 0:
            dick_vars["gameplay"].stop()
            dick_vars["game_over"].play()
            dick_vars["game_state"] = 2
    
    def aumentar_powerup(self, dick_vars:dict):
        if dick_vars["power_ups"] < 7:
            dick_vars["power_ups"] += 1
    
    def chequear_colisiones(self, dick_vars:dict):
        if self.rect.collidelist(dick_vars["lista_balas_enemigo_rect"]) != -1:
            self.bajar_vida(dick_vars)
            dick_vars["lista_balas_enemigo"][self.rect.collidelist(dick_vars["lista_balas_enemigo_rect"])].borrar_bala(dick_vars["lista_balas_enemigo"])
        if self.rect.collidelist(dick_vars["lista_enemigos_rect"]) != -1:
            self.bajar_vida(dick_vars)
            dick_vars["lista_enemigos"][self.rect.collidelist(dick_vars["lista_enemigos_rect"])].borrar_enemigo(dick_vars["lista_enemigos"])
