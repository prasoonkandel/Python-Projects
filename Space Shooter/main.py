# run this file to play game

import pygame
import time
from Objects.spaceship import Spaceship
from Objects.bullet import Bullet, create_new_bullet
from Objects.enemy import Enemy, create_new_enemy
from Objects.reload import Reload, create_new_reload

clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.font.init()
bullet_count_font = pygame.font.SysFont("Montserrat", 24)

# Constants
WIDTH, HEIGHT = 540, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
# loading sounds
fire_sound = pygame.mixer.Sound("assets/Sounds/fire.mp3")
bg_music = pygame.mixer.music.load("assets/Sounds/background.wav")
game_over_sound = pygame.mixer.Sound("assets/Sounds/game_over.mp3")
explosion_sound = pygame.mixer.Sound("assets/Sounds/explosion.wav")
pygame.mixer.music.play(-1)
# loding images
bullet_image = pygame.image.load("assets/Images/bullet.png").convert_alpha()
space_ship_image = pygame.image.load("assets/Images/ship.png").convert_alpha()
stars_image = pygame.image.load("assets/Images/stars.png").convert()
enemy_img = pygame.image.load("assets/Images/enemy.png").convert_alpha()
reload_img = pygame.image.load("assets/Images/reload.png").convert_alpha()
background_img = pygame.image = pygame.transform.scale(
    stars_image, (int(stars_image.get_width() * 0.2),
                  int(stars_image.get_height() * 0.2))
)

space_ship = Spaceship(space_ship_image, WIDTH//2, HEIGHT-100, 0.2)

fire_delay = 100
last_fired = 0
last_enemy_spawned = 0
last_reload_spawned = 0
score = 0
running = True
while running:
    clock.tick(60)
    pygame.display.set_caption(f"Space Shooter - FPS: {clock.get_fps():.2f}")
    bullet_count_text = f"Bullets: {Bullet.magaze}"
    score_text = f"Score: {score}"
    SCREEN.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                space_ship.fire(bullet_image, fire_sound)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        space_ship.move_left(SCREEN)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        space_ship.move_right(SCREEN)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        space_ship.move_up(SCREEN)

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        space_ship.move_down(SCREEN)
    space_key_pressed = keys[pygame.K_SPACE]
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - last_fired >= fire_delay:
        space_ship.fire(bullet_image, fire_sound)
        last_fired = current_time
    if pygame.time.get_ticks() - last_enemy_spawned >= 500:
        create_new_enemy(enemy_img, SCREEN_WIDTH=WIDTH)
        last_enemy_spawned = pygame.time.get_ticks()
    if pygame.time.get_ticks() - last_reload_spawned >= 7500:
        create_new_reload(reload_img, SCREEN_WIDTH=WIDTH)
        last_reload_spawned = pygame.time.get_ticks()
    # tracking collisions
    for enemy in Enemy.enemy_list:
        offset = (enemy.rect.x - space_ship.rect.x,
                  enemy.rect.y - space_ship.rect.y)
        if space_ship.mask.overlap(enemy.mask, offset):
            pygame.mixer.music.stop()
            Enemy.enemy_list.clear()
            Bullet.bullet_list.clear()
            Reload.reload_list.clear()
            space_ship.destroy()
            bullet_count_text = ""
            score_text = ""
            score_text2 = f"Score: {score}"
            score_surface2 = bullet_count_font.render(
                score_text2, True, (255, 255, 0))
            SCREEN.fill((0, 0, 0))
            font = pygame.font.SysFont("Montserrat", 64)
            text = font.render("GAME OVER", True, (255, 0, 0))
            SCREEN.blit(
                text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            SCREEN.blit(
                score_surface2, (WIDTH // 2 - text.get_width() // 2, (HEIGHT // 2)+70))
            pygame.display.flip()

            game_over_sound.play()

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 4500:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                clock.tick(60)
            running = False
            break

    for bullet in Bullet.bullet_list[:]:
        for enemy in Enemy.enemy_list[:]:
            offset = (bullet.rect.x - enemy.rect.x,
                      bullet.rect.y - enemy.rect.y)
            if bullet.mask.overlap(enemy.mask, offset):
                Bullet.destroy(bullet)
                Enemy.destroy(enemy)
                explosion_sound.play()
                score += 36
                break
    for reload in Reload.reload_list[:]:
        offset = (reload.rect.x - space_ship.rect.x,
                  reload.rect.y - space_ship.rect.y)
        if space_ship.mask.overlap(reload.mask, offset):
            Reload.reload_list.remove(reload)
            Bullet.magaze += 37
            if Bullet.magaze > 50:
                Bullet.magaze = 50
            break

    # showing images
    Reload.show(SCREEN)
    Enemy.show(SCREEN)
    Bullet.show_bullets(SCREEN)
    space_ship.show(SCREEN)
    text_surface = bullet_count_font.render(
        bullet_count_text, True, (255, 255, 255))
    SCREEN.blit(text_surface, (10, 10))
    score_surface = bullet_count_font.render(score_text, True, (255, 255, 0))
    SCREEN.blit(score_surface, (WIDTH // 2 -
                score_surface.get_width() // 2, 10))

    pygame.display.flip()
pygame.quit()
