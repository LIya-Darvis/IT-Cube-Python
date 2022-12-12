import pygame

# вызов библиотеки
pygame.init()

# создание окна
screen = pygame.display.set_mode((800, 600))

# название окна
pygame.display.set_caption("Space Breakers")

# картинка должна быть в той же папке, что и файл main.py
icon = pygame.image.load("blackhole.png")
pygame.display.set_icon(icon)

# игрок
playerImg = pygame.image.load("spaceship.png")
playerX = 340
playerY = 470
playerX_change = 0
# playerY_change = 0

# пули
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# функция создания игрока на заданных координатах
def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# начало работы программы
running = True  # создание флага
while running:
    for event in pygame.event.get():  # .event для любых событий pygame
        if event.type == pygame.QUIT:  # тип события - выход из программы
            running = False  # аналогично команде break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.1
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # if playerY <= 0:
    #     playerY = 0
    # elif playerY >= 536:
    #     playerY = 536

    playerX += playerX_change
    # playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()  # постоянное обновление окна
