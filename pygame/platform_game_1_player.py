import pygame, os

# inicjalizacja modułów pygame
pygame.init()

# stałe
SIZESCREEN = WIDTH, HEIGHT = 1280, 960
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
DARKGREEN = pygame.color.THECOLORS['darkgreen']

STAND_R = pygame.image.load(os.path.join('png', 'player_standR.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_standL.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'player_walkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'player_walkR2.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'player_walkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'player_walkL2.png'))
RIGHT_LIST = [WALK_R1, WALK_R2]
LEFT_LIST = [WALK_L1, WALK_L2]

screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, image, current_level=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.level = current_level
        self.count = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 6

    def turn_left(self):
        self.movement_x = -6

    def stop_x(self):
        self.movement_x = 0

    def update(self):
        self.rect.x += self.movement_x

        if self.movement_x > 0:
            self._move(RIGHT_LIST)

        if self.movement_x < 0:
            self._move(LEFT_LIST)

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count = 0
        else:
            self.count += 1

    def get_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            elif event.key == pygame.K_a:
                self.turn_left()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop_x()
                self.image = STAND_R
            elif event.key == pygame.K_a and self.movement_x < 0:
                self.stop_x()
                self.image = STAND_L


# konkretyzacja obiektów
player = Player(STAND_R)
player.rect.center = WIDTH // 2, HEIGHT // 2

# pętla gry
window_open = True

while window_open:
    screen.fill(LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        player.get_events(event)

        # rysowanie i aktualizacja obketów
    player.draw(screen)
    player.update()

    # aktualizacja głównego okna
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
