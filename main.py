import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

# игрок
playerImg = pygame.image.load("spaceship.png")
playerX = 340
playerY = 470
playerX_change = 0

# пули
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2


def fire_bullet(x, y):
    display.blit(bulletImg, (x + 16, y + 10))

def player(x, y):
    display.blit(playerImg, (x, y))

def run_game(playerX, playerY, playerX_change, bulletX, bulletY):
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.1
                if event.key == pygame.K_SPACE:
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        display.fill((5, 5, 10))

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        playerX += playerX_change

        player(playerX, playerY)
        pygame.display.update()

run_game(playerX, playerY, playerX_change, bulletX, bulletY)
