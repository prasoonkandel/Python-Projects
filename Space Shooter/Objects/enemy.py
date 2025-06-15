import pygame
import random
from pygame.sprite import Sprite


class Enemy(Sprite):
    enemy_list = []
    MAX_ENEMIES = 10

    def __init__(self, image, x=0, y=0, scale=0.1):
        super().__init__()
        self.speed = random.randint(2, 5)
        self.size = random.choice([0.075,  0.075, 0.1])
        self.image = pygame.transform.scale(
            image, (int(image.get_width() * self.size), int(image.get_height() * self.size)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.mask = pygame.mask.from_surface(self.image)

    def get_speed(self):
        return self.speed

    @staticmethod
    def check_for_off_screen(height=0):
        for enemy in Enemy.enemy_list:
            if enemy.rect.y > height:
                Enemy.enemy_list.remove(enemy)

    @staticmethod
    def move(screen_height):
        Enemy.check_for_off_screen(screen_height)
        for enemy in Enemy.enemy_list:
            enemy.rect.y += enemy.get_speed()

    def destroy(self):
        Enemy.enemy_list.remove(self)

    @staticmethod
    def show(screen):
        Enemy.move(screen_height=screen.get_height())
        for enemy in Enemy.enemy_list:
            screen.blit(enemy.image, enemy.rect)


def create_new_enemy(enemy_img, SCREEN_WIDTH=0):
    if len(Enemy.enemy_list) >= Enemy.MAX_ENEMIES:
        return
    x = random.randint(0 + 50, SCREEN_WIDTH - 50)
    y = random.randint(-500, -100)
    new_enemy = Enemy(enemy_img, x, y,)
    Enemy.enemy_list.append(new_enemy)
