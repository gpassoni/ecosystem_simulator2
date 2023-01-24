import pygame
from pygame.locals import *
from random import randint
import random
from random import randrange
import math
from time import sleep

WIDTH, HEIGHT = 1520, 785
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ecosystem Simulator!")

FPS = 60

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


slimy_background = pygame.image.load("slimybackground.jpg")

cell_image8 = pygame.image.load("monster8.png")
scaled_bacterio8 = scale_image(cell_image8, 0.1)

cell_image10 = pygame.image.load("batterio10_image.png")
scaled_bacterio10 = scale_image(cell_image10, 0.1)

cell_image11 = pygame.image.load("batterio11_image.png")
scaled_bacterio11 = scale_image(cell_image11, 0.1)


class Cell():
    CELLS_lst = []
    MASKS_lst = []

    def __init__(self, color, max_vel, rotation_vel):

        self.img = random.choice([scaled_bacterio8, scaled_bacterio10, scaled_bacterio11])

        self.color = color
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.side = 60
        self.vel = 0
        self.angle = 0
        self.x = randint(self.side + 10, WIDTH - self.side - 10)
        self.y = randint(self.side + 10, HEIGHT - self.side - 10)
        self.acceleration = 0.1
        self.action = False
        self.action_end = 0
        self.choice = None
        self.security_side = 125
        self.side_tollerance = 5

    def collide(self, mask, x=0, y=0):
        cel_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(cel_mask, offset)
        return poi

    @classmethod
    def spawncells(cls, number):
        for i in range(number):
            cell = Cell(random.choice([GREEN, BLUE, BLACK, PURPLE, YELLOW]), 2, 1)
            cls.CELLS_lst.append(cell)
        return cls.CELLS_lst

    def decide(self):
        if self.action is False:
            self.action_end = pygame.time.get_ticks() + randint(1, 4) * 1000
            self.choice = random.choice(["right", "left", "forward"])
            self.action = True

        if current >= self.action_end:
            self.action = False

        if self.choice == "right":
            self.rotate(right=True)
        elif self.choice == "left":
            self.rotate(left=True)
        elif self.choice == "forward":
            self.rotate()

    def draw(self, win):
        # pygame.draw.rect(win, self.color, (self.x, self.y, self.side, self.side))
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        self.lateral_collisions()
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def lateral_collisions(self):
        # tocca a sinistra
        if self.x <= self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.x <= self.side_tollerance:
                self.angle += 90

        # tocca a destra
        if self.x + self.side >= WIDTH - self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.x + self.side >= WIDTH - self.side_tollerance:
                self.angle += 90

        # tocca sopra
        if self.y <= self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.y <= self.side_tollerance:
                self.angle += 90

        # toca sotto
        if self.y + self.side >= HEIGHT - self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.y + self.side >= HEIGHT - self.side_tollerance:
                self.angle += 90


all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
collisions = [all_sprites, collision_sprites]


def draw(win, cells_list):
    WIN.blit(slimy_background, (0, 0))

    for cell in cells_list:
        cell.draw(win)

    pygame.display.update()


if __name__ == '__main__':
    clock = pygame.time.Clock()
    images = [()]
    run = True

    cells = Cell.spawncells(2)

    pygame.init()

    while run:
        clock.tick(FPS)

        WIN.fill(WHITE)
        draw(WIN, cells)
        sleep(1)
        for i in Cell.CELLS_lst:
            print(i.x)
        current = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        for cell in cells:
            cell.move_forward()
            cell.decide()

    pygame.quit()
