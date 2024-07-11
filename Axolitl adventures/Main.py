import pygame
from Class_jugador import Player
from Class_event_handler import EventHandler
from Class_Graficos import Graficos
from Class_bala import Bala
from Class_enemies import Enemigo
from Class_bala_enemigo import Bala_enemigo

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()



#To do: Add a waves
#To do: Add enemies
#To do: Add a score
#To do: Game over (a medias)
#To do: Add a high score
#To do: Use powerups
#To do: Use Files


pygame.display.set_caption("Axolitl adventures")
pantalla = pygame.display.set_mode((800, 600))

dick_vars = {
    "running" : True,

    "boton_jugar" : None,
    "boton_mutear" : None,

    "jugador" : Player(0, 0),

    "lista_balas" : [],

    "game_state" : 0,

    "mute" : False,
    "intro" : pygame.mixer.Sound("Axolitl Adventures/Assets/Music/Intro.mp3"),
    "game_over" : pygame.mixer.Sound("Axolitl Adventures/Assets/Music/Game Over.mp3"),
    "disparo" : pygame.mixer.Sound("Axolitl Adventures/Assets/Music/Disparo.mp3"),
    "gameplay" : pygame.mixer.Sound("Axolitl Adventures/Assets/Music/Game Music.mp3"),


    "fuente" : pygame.font.Font("Axolitl Adventures/Assets/Graficos/Sans.ttf", 30),

    "score" : 0,

    "vida" : 3,

    "power_ups" : 0,

    "Waves" : [],
    "lista_enemigos" : [],
    "lista_balas_enemigo" : [],

    "lista_balas_rect": [],
    "lista_enemigos_rect": [],
    "lista_balas_enemigo_rect": [],
}
dick_vars["intro"].set_volume(0.08)
dick_vars["disparo"].set_volume(0.5)
dick_vars["gameplay"].set_volume(0.04)
dick_vars["game_over"].set_volume(0.05)
dick_vars["intro"].play(-1)
Enemigo([600, 300], "Axolitl Adventures/Assets/Graficos", 3, dick_vars)
while dick_vars["running"]:
    EventHandler(dick_vars, pygame.event.get())
    pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Fondo.png"), (0, 0))
    if dick_vars["game_state"] == 0:
        dick_vars["boton_jugar"] = pygame.draw.rect(pantalla, (0, 255, 255), (300, 300, 200, 70))
        Graficos.render_fuente( "Jugar", dick_vars["fuente"], (0, 0, 0), pantalla, (356, 315))
        pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Logo.png"), (254, 75))
        dick_vars["boton_mutear"] = pygame.draw.rect(pantalla, (0, 255, 255), (700, 25, 70, 70))
        pantalla.blit(pygame.image.load("Axolitl Adventures/Assets/Graficos/Mute button.png"), (700, 25))
    elif dick_vars["game_state"] == 1:
        Graficos.dibujar_lista_balas(dick_vars["lista_balas"], pantalla, dick_vars)
        Graficos.calcular_rects(dick_vars)
        Graficos.dibujar_jugador(dick_vars["jugador"], pantalla, dick_vars)
        Graficos.dibujar_vida(dick_vars, pantalla)
        Graficos.dibujar_lista_enemigos(dick_vars["lista_enemigos"], pantalla, dick_vars)
        Graficos.dibujar_lista_balas_enemigos(dick_vars["lista_balas_enemigo"], pantalla, dick_vars)
    elif dick_vars["game_state"] == 2:
        pygame.draw.rect(pantalla, (0, 0, 0), (0, 0, 800, 600))
        dick_vars["boton_jugar"] = pygame.draw.rect(pantalla, (0, 255, 255), (275, 300, 250, 70))
        Graficos.render_fuente( "Jugar de nuevo?", dick_vars["fuente"], (0, 0, 0), pantalla, (282, 315))
        Graficos.render_fuente( "Game Over", dick_vars["fuente"], (255, 0, 0), pantalla, (325, 75))

    pygame.display.update()
    clock.tick(30)
    

pygame.mixer.quit()
pygame.quit()