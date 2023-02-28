import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_run1 = pygame.image.load(r"assets/images/dinorun1.png")
        self.image_run2 = pygame.image.load(r"assets/images/dinorun2.png")

        self.image = self.image_run1

        self.surface = pygame.display.get_surface()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = self.surface.get_rect().midleft
        self.rect.left += self.surface.get_width()/10
        self.rect.bottom += 5
        self.step = 0
        self.height = 15
        self.jumping = False
        self.sound_jump = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.sound_die = pygame.mixer.Sound('assets/sounds/die.wav')

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.step += 1
        if self.step % 10 == 0:
            self.image = self.image_run1 if self.image == self.image_run2 else self.image_run2

        # if self.image == self.image_run1:
        #     self.image = self.image_run2
        # else:
        #     self.image = self.image_run1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.sound_jump.play()
            self.jumping = True
        if self.jumping:
            self.jump()

    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False

