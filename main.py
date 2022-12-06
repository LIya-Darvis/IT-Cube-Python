import pygame
# вызов библиотеки
pygame.init()
# создание окна
screen = pygame.display.set_mode((800, 600))
# добавляем название
pygame.display.set_caption("Space Stalkers")
# добавляем иконку
icon = pygame.image.load("aircraft.png")
pygame.display.set_icon(icon)
# параметры отображения персонажа
playerImg = pygame.image.load("taco.png")
playerX = 340
playerY = 470
playerX_change = 0
playerY_change = 0

# функция отображения персонажа в окне
def player(x, y):
    screen.blit(playerImg, (x, y))

# начало работы программы
running = True  # флаг для последующего закрытия
while running:
    for event in pygame.event.get():  # определяем тип события
        if event.type == pygame.QUIT:  # тип события: закрытие окна
            running = False  # аналогично команде break
        if event.type == pygame.KEYDOWN:  # тип события: нажатие кнопки
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1

            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    player(playerX, playerY)
    pygame.display.update()  # постоянное обновление окна
