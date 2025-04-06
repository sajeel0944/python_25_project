import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space invadors")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load("space-invaders.png")
platerX = 150
playerY = 400


def player():
    screen.blit(player_img, (platerX, playerY))


running = True 
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()