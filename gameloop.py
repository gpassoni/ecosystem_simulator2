import images_processor
from global_variables import *
from cell_abstract import Cell

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ecosystem Simulator!")

FPS = 60

all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
collisions = [all_sprites, collision_sprites]


def draw(win, cells_list):
    WIN.blit(images_processor.slimy_background, (0, 0))

    for cell in cells_list:
        cell.draw(win)

    pygame.display.update()


if __name__ == '__main__':
    clock = pygame.time.Clock()
    images = [()]
    run = True

    cellsinstance = Cell()
    cells = cellsinstance.spawncells(10)

    print(cells)

    pygame.init()

    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)
        current = pygame.time.get_ticks()

        draw(WIN, cells)
        for i in Cell.CELLS_lst:
            # print(i.x)
            pass

        if len(cells) == 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        for cell in cells:
            cell.move_forward()
            cell.decide(current)

    pygame.quit()
