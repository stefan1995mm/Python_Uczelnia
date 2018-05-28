import pygame, os

clock = pygame.time.Clock()
# inicjalizacja modułów pygame
pygame.init()

# stałe
SIZESCREEN = WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set_mode(SIZESCREEN)

STAND_R = pygame.image.load(os.path.join('png', 'player_standR.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_standL.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'player_walkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'player_walkL2.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'player_walkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'player_walkR2.png'))

# kolory
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
image_left = [WALK_L1, WALK_L2]
image_right = [WALK_R1, WALK_R2]

pygame.display.set_caption('Prosta gra platformowa')


class Player(pygame.sprite.Sprite):

    def __init__(self, image, current_lever=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.level = current_lever
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_left(self):
        self.movement_x = -6

    def turn_right(self):
        self.movement_x = 6

    def stop_x(self):
        self.movement_x = 0

    def stop_y(self):
        self.movement_y = 0

    def update(self):
        # --------ruch w pionie-------#
        self.rect.x += self.movement_x
        # animacja
        if self.movement_x > 0:
            self._move(image_right)
        if self.movement_x < 0:
            self._move(image_left)
        # -------------------------

    def _move(self, list_image):
        if self.count < 4:
            self.image = list_image[0]
        elif self.count < 8:
            self.image = list_image[1]

        if self.count >= 8:
            self.count = 0
        else:

            self.count += 1

    def get_event(self, event):
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


class Level:
    def __init__(self):
        self.set_of_platforms = set()

    def draw(self, surface):
        for el in self.set_of_platforms:
            el.draw(surface)


class Level_1(Level):
    def __init__(self):
        super().__init__()
        self.platforms = [[1120, 70, 50, HEIGHT - 70], [280, 70, 100, 300]]

        for el in self.platforms:
            self.set_of_platforms.add(Platform(DARKGREEN, *el))


class Platform(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, rect_x, rect_y):
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.colour = colour
        self.image.fill(self.colour)
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)


current_level = Level_1()
player = Player(STAND_R)
player.rect.center = WIDTH // 2, HEIGHT // 2
WINDOW_OPEN = True

while WINDOW_OPEN:
    screen.fill(LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WINDOW_OPEN = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                WINDOW_OPEN = False
        player.get_event(event)
    player.draw(screen)
    # current_level.draw()
    player.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
