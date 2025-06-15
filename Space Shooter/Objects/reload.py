import pygame
import random
from pygame.sprite import Sprite


class Reload(Sprite):
    reload_list = []
    MAX_RELOADS = 1

    def __init__(self, image, x=0, y=0, scale=0.1):
        super().__init__()
        self.speed = 5
        self.size = 0.1
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
        for reload in Reload.reload_list:
            if reload.rect.y > height:
                reload.reload_list.remove(reload)

    @staticmethod
    def move(screen_height):
        Reload.check_for_off_screen(screen_height)
        for reload in Reload.reload_list:
            reload.rect.y += reload.get_speed()

    def destroy(self):
        Reload.reload_list.remove(self)

    @staticmethod
    def show(screen):
        Reload.move(screen_height=screen.get_height())
        for reload in Reload.reload_list:
            screen.blit(reload.image, reload.rect)


def create_new_reload(reload_img, SCREEN_WIDTH=0):
    if len(Reload.reload_list) >= Reload.MAX_RELOADS:
        return
    x = random.randint(0 + 50, SCREEN_WIDTH - 50)
    y = random.randint(-500, -100)
    new_reload = Reload(reload_img, x, y,)
    Reload.reload_list.append(new_reload)
