import random
import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/cloud.png")
        self.rect = self.image.get_rect()

        self.surface = pygame.display.get_surface()
        rand_width = random.randint(0, self.surface.get_width())
        rand_height = random.randint(0, self.surface.get_height() / 2)
        self.rect.midleft = (rand_width, rand_height)
        self.speed = random.randint(2, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            rand_height = random.randint(0, self.surface.get_height() / 2)
            self.rect.midleft = (self.surface.get_width(), rand_height)
