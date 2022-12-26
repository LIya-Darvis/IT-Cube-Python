import math
import random
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
bulletY_change = 10

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.05)
    enemyY_change.append(20)



def fire_bullet(x, y):
    display.blit(bulletImg, (x + 16, y + 10))

def player(x, y):
    display.blit(playerImg, (x, y))

def enemy(x, y, i):
    display.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def run_game(playerX, playerY, playerX_change, bulletX, bulletY):
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.8
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.8
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


        for i in range(num_of_enemies):

            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.5
                enemyY[i] += enemyY_change[i]

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)


        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        playerX += playerX_change

        player(playerX, playerY)
        pygame.display.update()

run_game(playerX, playerY, playerX_change, bulletX, bulletY)
