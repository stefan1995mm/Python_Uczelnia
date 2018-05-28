import pygame, os

os.environ['SDL_VIDEO_CENTERED0'] = '1'  # wyśrodkowanie okna pygame
# inicjalizacja modułów pygame
pygame.init()

# stałe
SCREENSIZE = WIDTH, HEIGHT = 1280, 650
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('Prosta gra platformowa...xD')
clock = pygame.time.Clock()

# kolory
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
DRAKGREEN = pygame.color.THECOLORS['darkgreen']

STAND_R = pygame.image.load(os.path.join('png', 'player_standR.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_standL.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'player_walkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'player_walkL2.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'player_walkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'player_walkR2.png'))

image_left = [WALK_L1, WALK_L2]
image_right = [WALK_R1, WALK_R2]


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.level = None
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.on_platform = False
        self.direction_of_movement = 'right'

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_left(self):
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -6

    def turn_right(self):
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 6

    def stop_x(self):
        self.movement_x = 0

    def stop_y(self):
        self.movement_y = 0

    def jump(self):
        if self.on_platform:
            self.movement_y = - 13

    def update(self):
        self._gravitation()
        # --------------- ruch w poziomie ----------------
        self.rect.x += self.movement_x
        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for platform in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = platform.rect.left
            if self.movement_x < 0:
                self.rect.left = platform.rect.right

        # --------------- animacja ----------------
        if self.movement_x > 0:
            self._move(image_right)
        if self.movement_x < 0:
            self._move(image_left)

        # ----------------------------------------------
        # -----ruch w pionie ---------------------------
        self.rect.y += self.movement_y

        colliding_platforms = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for platform in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = platform.rect.top
            if self.movement_y < 0:
                self.rect.top = platform.rect.bottom

            self.stop_y()
        # czy jestesmy na platformie
        self.rect.y += 4
        if pygame.sprite.spritecollide(self, self.level.set_of_platforms, False):
            self.on_platform = True
        else:
            self.on_platform = False
        self.rect.y -= 4

        # -----------------------------------------------

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
            elif event.key == pygame.K_w:
                self.jump()


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop_x()
                self.image = STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop_x()
                self.image = STAND_L

    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 2
        else:
            self.movement_y += 0.35


class Level:  # trap adventure
    def __init__(self, player):
        self.player = player
        self.set_of_platforms = set()
        # pygame.sprite.Group()

    def draw(self, surface):
        for el in self.set_of_platforms:
            el.draw(surface)


class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        self.platforms = [[1120, 70, 50, HEIGHT - 70], [280, 70, 100, 300],
                          [350, 70, 200, 600], [210, 70, 900, 700],
                          [280, 70, 800, 500]]

        for el in self.platforms:
            self.set_of_platforms.add(Platform(DRAKGREEN, *el))


class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, hight, rect_x, rect_y):
        self.image = pygame.Surface([width, hight])
        self.rect = self.image.get_rect()
        self.color = color
        self.image.fill(self.color)
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# konkrteyzacja obiektów
player = Player(STAND_R)
player.rect.center = WIDTH // 2, HEIGHT // 2
current_level = Level_1(player)
player.level = current_level
# player

# główna pętla gry
window_open = True

while window_open:
    screen.fill(LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        player.get_event(event)
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    # rysowanie i aktualizacja obiektów
    current_level.draw(screen)
    player.draw(screen)
    player.update()

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
