import pygame
import random

def draw_window(win, background, player_img, player, bullets, enemies):
    win.blit(background, (0, 0))
    win.blit(player_img, (player.x, player.y))

    for bullet in bullets:
        pygame.draw.rect(win, (255, 0, 0), bullet)

    for enemy in enemies:
        win.blit(enemy["img"], enemy["rect"])

    pygame.display.update()

def handle_bullets(bullets, enemies):
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)
        for enemy in enemies[:]:
            if bullet.colliderect(enemy["rect"]):
                try:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                except ValueError:
                    pass

def handle_enemies(enemies, width):
    if len(enemies) < 5:
        new_enemy = {
            "rect": pygame.Rect(random.randint(0, width - 50), 0, 50, 50),
            "img": pygame.image.load("assets/enemy.png")
        }
        enemies.append(new_enemy)

    for enemy in enemies:
        enemy["rect"].y += 1

def draw_menu(win):
    win.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 55)
    text = font.render("Presiona ENTER para jugar", True, (255, 255, 255))
    win.blit(text, (200, 250))
    pygame.display.update()

def draw_game_over(win):
    win.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 60)
    text = font.render("¡Game Over! Presiona ENTER para reiniciar", True, (255, 0, 0))
    win.blit(text, (100, 250))
    pygame.display.update()
