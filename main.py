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

# функция создания игрока на заданных координатах
def player(x, y):
    screen.blit(playerImg, (x, y))

# начало работы программы
running = True  # создание флага
while running:
    for event in pygame.event.get():  # .event для любых событий pygame
        if event.type == pygame.QUIT:  # тип события - выход из программы
            running = False  # аналогично команде break

    player(playerX, playerY)
    pygame.display.update()  # постоянное обновление окна
