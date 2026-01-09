import pygame
import sys
import random

# 1. INICIALIZAR
pygame.init()
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Misión Espacial - ¡ESQUIVA!")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# --- JUGADOR ---
jugador_x = 375
jugador_y = 500
jugador_ancho = 50
jugador_alto = 50
velocidad = 6

# --- ENEMIGO ---
enemigo_ancho = 50
enemigo_alto = 50
enemigo_x = random.randint(0, ANCHO - enemigo_ancho)
enemigo_y = 0
enemigo_velocidad = 8

# ---PUNTAJE ---
puntaje = 0
fuente = pygame.font.SysFont("monospace", 35) # Tipo de letra para el marcador

reloj = pygame.time.Clock()
game_over = False

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True

    # --- A. MOVIMIENTOS ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_ancho:
        jugador_x += velocidad

    enemigo_y += enemigo_velocidad

    # Respawn del enemigo (Si toca el suelo)
    if enemigo_y > ALTO:
        enemigo_y = 0
        enemigo_x = random.randint(0, ANCHO - enemigo_ancho)
        puntaje += 1 # ¡Ganaste un punto por esquivarlo!
        enemigo_velocidad += 0.5 # ¡SE PONE MÁS DIFÍCIL! (Aumentamos velocidad)

    # --- B. CREAR LOS RECTÁNGULOS INVISIBLES (HITBOXES) ---
    # Para detectar el choque, necesitamos crear los objetos "Rect" oficiales de Pygame
    jugador_rect = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)
    enemigo_rect = pygame.Rect(enemigo_x, enemigo_y, enemigo_ancho, enemigo_alto)

    # --- C. DETECTAR COLISIÓN ---
    if jugador_rect.colliderect(enemigo_rect):
        print("💥 ¡BOOM! CHOCASTE 💥")
        print(f"Puntaje Final: {puntaje}")
        game_over = True # Rompe el ciclo y cierra el juego

    # --- D. DIBUJAR ---
    pantalla.fill(NEGRO)
    
    pygame.draw.rect(pantalla, ROJO, jugador_rect)
    pygame.draw.rect(pantalla, AZUL, enemigo_rect)

    # Dibujar el puntaje en pantalla (Texto amarillo)
    texto = fuente.render(f"Puntos: {puntaje}", 1, AMARILLO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()