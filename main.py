import pygame
import random
from utils import draw_window, handle_bullets, handle_enemies, draw_menu, draw_game_over

# Inicialización de PyGame
pygame.init()

# Constantes de pantalla
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars")

# Colores y FPS
WHITE = (255, 255, 255)
FPS = 60

# Cargar imágenes
PLAYER_IMG = pygame.image.load("assets/player.png")
ENEMY_IMG = pygame.image.load("assets/enemy.png")
BACKGROUND = pygame.image.load("assets/background.png")

# Jugador
player = pygame.Rect(375, 500, 50, 50)
player_speed = 5
bullets = []

# Enemigos
enemies = []

# Estados del juego
MENU, PLAYING, PAUSED, GAME_OVER = "menu", "playing", "paused", "game_over"
state = MENU

def main():
    global state
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        if state == MENU:
            draw_menu(WIN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    state = PLAYING

        elif state == PLAYING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullets.append(pygame.Rect(player.x + 20, player.y, 5, 10))
                    if event.key == pygame.K_p:
                        state = PAUSED

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - player_speed > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.x + player_speed < WIDTH - player.width:
                player.x += player_speed

            handle_bullets(bullets, enemies)
            handle_enemies(enemies, WIDTH)

            draw_window(WIN, BACKGROUND, PLAYER_IMG, player, bullets, enemies)

            if any(enemy["rect"].y > HEIGHT for enemy in enemies):
                state = GAME_OVER

        elif state == PAUSED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    state = PLAYING

        elif state == GAME_OVER:
            draw_game_over(WIN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    player.x = 375
                    bullets.clear()
                    enemies.clear()
                    state = PLAYING

    pygame.quit()

if __name__ == "__main__":
    main()
