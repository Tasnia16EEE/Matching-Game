import pygame
from time import sleep

import pygame
from pygame import display, event, image, mixer

import config as gc
from universities import University


def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index

pygame.init()
display.set_caption('My Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
matched = image.load('other_source/matched.png')
running = True
tiles = [University(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images_displayed = []
click_sound = pygame.mixer.Sound("click sound.ogg")

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col, index = find_index_from_xy(mouse_x, mouse_y)
            click_sound.play()
            if index not in current_images_displayed:
                if len(current_images_displayed) > 1:
                    current_images_displayed = current_images_displayed[1:] + [index]
                else:
                    current_images_displayed.append(index)

    # Display animals
    screen.fill((0, 0, 0))

    total_skipped = 0

    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1

    display.flip()

    # Check for matches
    if len(current_images_displayed) == 2:
        idx1, idx2 = current_images_displayed
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            # display matched message
            sleep(0.2)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.5)
            current_images_displayed = []

    if total_skipped == len(tiles):
        running = False

print('Goodbye!')
