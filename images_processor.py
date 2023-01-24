from global_variables import *


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


slimy_background = pygame.image.load("assets/slimybackground.jpg")

cell_image8 = pygame.image.load("assets/monster8.png")
scaled_bacterio8 = scale_image(cell_image8, 0.1)

cell_image10 = pygame.image.load("assets/batterio10_image.png")
scaled_bacterio10 = scale_image(cell_image10, 0.1)

cell_image11 = pygame.image.load("assets/batterio11_image.png")
scaled_bacterio11 = scale_image(cell_image11, 0.1)
