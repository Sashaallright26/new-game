import random

import pygame
import os


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        images = ['largecactus1.png', 'largecactus2.png', 'largecactus3.png',
                  'smallcactus1.png', 'smallcactus2.png', 'smallcactus3.png']
        image_path = os.path.join('assets/images', random.choice(images))
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.surface = pygame.display.get_surface()
        self.rect.left, self.rect.bottom = self.surface.get_rect().midleft
        self.rect.left += self.surface.get_width() * 2
        self.rect.bottom += 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 5

        if self.rect.right < 0:
            self.kill()
