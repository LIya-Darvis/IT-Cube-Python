import pygame

# вызов библиотеки
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Stalkers")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 470

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
