''' Персонажи: герой (управляется стрелками), препятствия (стоят), враги (случайно перемещаются), мины (стоят).
класс Enemy - строки 66 - 78
мины - те же wall, но добавлены в список мин!
заведены следующие группы спрайтов: all_sprites, barriers, enemies, bombs
'''

# Подключить нужные модули
from random import randint # враги будут случайно перемещаться
import pygame 
pygame.init() 

# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
# left_bound = win_width / 40             # границы, за которые персонаж не выходит (начинает ехать фон)
# right_bound = win_width - left_bound

img_file_back = 'cave.png'
img_file_hero = 'm1.png'
img_file_enemy = 'enemy.png'  # картинка для врага
FPS = 60

# цвета:
C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)

# shift = 0

# Классы
class Hero(pygame.sprite.Sprite):
    def __init__(self, filename, x_speed=0, y_speed=0, x=20, y=0, width=120, height=120):
        pygame.sprite.Sprite.__init__(self)
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha() 
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        self.rect = self.image.get_rect()
        # ставим персонажа в переданную точку (x, y):
        self.rect.x = x 
        self.rect.y = y
        # создаем свойства, запоминаем переданные значения:
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        pygame.sprite.Sprite.__init__(self)
        # картинка - новый прямоугольник нужных размеров:
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # создаем свойство rect 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

class Enemy(pygame.sprite.Sprite): # враг
    def __init__(self, x=20, y=0, filename=img_file_enemy, width=120, height=120):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)

# Запуск игры
pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode([win_width, win_height])

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 

# список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# список препятствий:
barriers = pygame.sprite.Group()
# список врагов:
enemies = pygame.sprite.Group()
# список мин:
bombs = pygame.sprite.Group()

# создаем персонажа, добавляем его в список всех спрайтов:
robin = Hero(img_file_hero) 
all_sprites.add(robin)
# создаем стены, добавляем их:
w = Wall(50, 150, 480, 50)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360)
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 400, 640, 50)
barriers.add(w)
all_sprites.add(w)

# создаем врагов, добавляем их:
en = Enemy(50, 480)
all_sprites.add(en)
enemies.add(en)

en = Enemy(380, 480)
all_sprites.add(en)
enemies.add(en)

# создаем мины, добавляем их:
bomb = Wall(x=550, y=460, color=C_RED)
bombs.add(bomb) # в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой


# Основной цикл игры:
timer = pygame.time.Clock() 
run = True 

while run:
    # Ввод данных (обработка событий)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                robin.x_speed = -5 
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 5 
            elif event.key == pygame.K_UP:
                robin.y_speed = -5 
            elif event.key == pygame.K_DOWN:
                robin.y_speed = 5 

        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                robin.x_speed = 0
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 0
            elif event.key == pygame.K_UP:
                robin.y_speed = 0
            elif event.key == pygame.K_DOWN:
                robin.y_speed = 0

    # Вычисления:
    # перемещение игровых объектов, 
    all_sprites.update()

    # Вывод данных (отрисовка)
    # рисуем фон
    window.blit(back, (0, 0)) 

    # сверху фона размещаем все спрайты на своих местах:
    all_sprites.draw(window)
    bombs.draw(window) # группу бомб рисуем отдельно - так бомба, 
                       # которая ушла из своей группы, автоматически перестанет быть видимой!
    
    pygame.display.update() 

    # Пауза
    timer.tick(FPS)
