from global_variables import *
from images_processor import *
from uuid import uuid4


class Cell:
    CELLS_lst = []

    def __init__(self):
        self.img = random.choice([scaled_bacterio8, scaled_bacterio10, scaled_bacterio11])

        self.name = str(uuid4())

        # movement
        self.max_vel = 2
        self.rotation_vel = 1
        self.acceleration = 0.1
        self.vel = 0
        self.angle = 0

        self.action = False
        self.action_end = 0
        self.choice = None

        # dimensions and collisions
        self.side = 60
        self.security_side = 125
        self.side_tollerance = 5

        # positions
        self.x = randint(self.side + 10, WIDTH - self.side - 10)
        self.y = randint(self.side + 10, HEIGHT - self.side - 10)
        self.population = []
        self.count = len(self.CELLS_lst)

    def get_positions(self):
        for i in self.population:
            print(f"{i.x}, {i.y}")

    def add_cell(self, cll):
        self.population.append(cll)

    def spawncells(self, number):
        for i in range(number):
            cell = Cell()
            self.CELLS_lst.append(cell)
            self.add_cell(cell)
        return self.CELLS_lst

    def decide(self, current):
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
        # pygame.draw.rect(win, BLACK, (self.x, self.y, self.side, self.side))
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel

    def end_game(self):
        if self.count == 0:
            pygame.quit()

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        # self.lateral_collisions()
        self.despown()

        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def despown(self):
        if self.x <= self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.x <= self.side_tollerance:
                self.CELLS_lst.remove(self)

        if self.x + self.side >= WIDTH - self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.x + self.side >= WIDTH - self.side_tollerance:
                self.CELLS_lst.remove(self)

        if self.y <= self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.y <= self.side_tollerance:
                self.CELLS_lst.remove(self)


        if self.y + self.side >= HEIGHT - self.security_side:
            self.vel = max(self.vel - self.acceleration * 2, 1.5)
            if self.y + self.side >= HEIGHT - self.side_tollerance:
                self.CELLS_lst.remove(self)

    """"
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

        for j in self.CELLS_lst:
            if j.name == self.name:
                pass
            else:

                #frontal collision
                x_offset = j.x - self.x
                y_offset = j.y - self.y
                if abs(x_offset) < 60 and abs(y_offset) < 60:
                    self.angle += 90
                    j.angle += 90
    """""
