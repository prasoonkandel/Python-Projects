import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    speed = 10
    bullet_list = []
    magaze = 50

    def __init__(self, image, x=0, y=0, scale=1):
        super().__init__()
        self.image = pygame.transform.scale(
            image, (int(image.get_width() * scale),
                    int(image.get_height() * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.mask = pygame.mask.from_surface(self.image)

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, screen):
        self.rect.y -= self.speed

    @staticmethod
    def show_bullets(screen):
        # move
        for bullet in Bullet.bullet_list:
            if bullet.rect.y <= 0:
                Bullet.remove_bullet(bullet)
            else:
                bullet.move(screen)
        # show
        for bullet in Bullet.bullet_list:

            bullet.show(screen)

    def destroy(self):
        Bullet.bullet_list.remove(self)

    @classmethod
    def remove_bullet(cls, bullet):

        cls.bullet_list.remove(bullet)

    @classmethod
    def decrease_magaze(cls):
        cls.magaze -= 1


def create_new_bullet(bullet_img, x, y):
    new_bullet = Bullet(bullet_img, x, y, 0.1)
    Bullet.bullet_list.append(new_bullet)
    Bullet.decrease_magaze()
