import sys

import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"Score {self.points}", True, (83, 83, 83))
        self.rect = self.image.get_rect()

        self.surface = pygame.display.get_surface()
        self.rect.bottomleft = (self.surface.get_width() / 1.5, self.surface.get_height() / 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1
            self.image = self.font.render(f"Score {self.points}", True, (83, 83, 83))


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def over(self, func):
        clock = pygame.time.Clock()
        while True:
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                func()


class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("assets/fonts/gamefont.ttf", 40)
        self.image = self.font.render(f"GAME OVER", True, (83, 83, 83))
        self.rect = self.image.get_rect()

        self.surface = pygame.display.get_surface()
        self.rect.bottomleft = (self.surface.get_width() / 4, self.surface.get_height() / 3.8)

    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Reset(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/reset.png")
        self.rect = self.image.get_rect()
        self.surface = pygame.display.get_surface()
        self.surface = pygame.display.get_surface()
        self.rect.bottomleft = (self.surface.get_width() / 2.13, self.surface.get_height() / 2.5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
