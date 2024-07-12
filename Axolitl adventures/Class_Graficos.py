import pygame
from Class_enemies import Enemigo

class Graficos:
    
    def dibujar_lista_balas(lista_balas:list, pantalla:pygame.Surface, dick_vars:dict):
        for bala in lista_balas:
            bala.mover_bala(dick_vars)
            bala.actualizar_animacion()
            bala.dibujar_bala(pantalla)
            

    def dibujar_jugador(jugador, pantalla, dick_vars:dict):
        jugador.dibujar(pantalla)
        jugador.bajar_cooldown()
        jugador.chequear_colisiones(dick_vars)

    def render_fuente(texto, fuente, color, superficie, posicion):
        render = fuente.render(texto, True, color)
        superficie.blit(render, posicion)

    def dibujar_vida(dick_vars:dict, pantalla):
        vida = dick_vars["jugador"].vida
        match vida:
            case 3:
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (10, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (80, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (150, 20))
            case 2:
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (10, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (80, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon vacio.png"), (150, 20))
            case 1:
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon amado.png"), (10, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon vacio.png"), (80, 20))
                pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Corazon vacio.png"), (150, 20))
    

    def dibujar_lista_enemigos(lista_enemigos:list, pantalla:pygame.Surface, dick_vars:dict):
        for enemigo in lista_enemigos:
            enemigo.enemigo_mover()
            enemigo.dibujar(pantalla)
            enemigo.enemigo_shootear(dick_vars)
            enemigo.bajar_cooldown()
            enemigo.chequear_colisiones(dick_vars)
            
    def dibujar_lista_balas_enemigos(lista_balas_enemigos:list, pantalla:pygame.Surface, dick_vars:dict):
        for balas in lista_balas_enemigos:
            balas.actualizar_animacion()
            balas.dibujar_bala_enemigo(pantalla)
            balas.mover_bala_enemigo(dick_vars)
    
    def calcular_rects(dick_vars:dict):
        dick_vars["jugador"].rect = dick_vars["jugador"].image.get_rect(topleft=[dick_vars["jugador"].x , dick_vars["jugador"].y] )
        dick_vars["lista_balas_enemigo_rect"] = []
        for bala in dick_vars["lista_balas_enemigo"]:
            dick_vars["lista_balas_enemigo_rect"].append(bala.image.get_rect(topleft=bala.pos))
        dick_vars["lista_enemigos_rect"] = []
        for enemigo in dick_vars["lista_enemigos"]:
            enemigo.rect = enemigo.image.get_rect(topleft=enemigo.pos)
            dick_vars["lista_enemigos_rect"].append(enemigo.image.get_rect(topleft=enemigo.pos))
        dick_vars["lista_balas_rect"] = []
        for bala in dick_vars["lista_balas"]:
            dick_vars["lista_balas_rect"].append(bala.image.get_rect(topleft=[bala.pos[0], int(bala.pos[1])]))
        dick_vars["lista_powerups_rect"] =[]
        for powerup in dick_vars["lista_powerups"]:
            powerup.rect = powerup.image.get_rect(topleft=powerup.pos)
            dick_vars["lista_powerups_rect"].append(powerup.image.get_rect(topleft=powerup.pos))

    def dibujar_lista_powerups(lista_powerups:list, pantalla:pygame.Surface, dick_vars:dict):
        for powerup in lista_powerups:
            powerup.dibujar_powerup(pantalla)
            powerup.mover_powerup(dick_vars)
    
    def chequear_cantidad_enemigos(dick_vars:dict):
        if len(dick_vars["lista_enemigos"]) == 0:
            Enemigo.generar_wave(dick_vars)