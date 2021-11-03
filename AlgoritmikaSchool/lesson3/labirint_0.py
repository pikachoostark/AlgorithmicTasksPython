''' Персонажи: герой (управляется стрелками), препятствия (стоят)
Добавили константы для цветов в формате (R,G,B) - строки 21 - 26, 
класс Wall (строки 52 - 62)
группу спрайтов barriers (препятствия), создание стен (строки 78 - 87)
Смещение фона пока убираем. 
'''
# Подключить нужные модули
import pygame 
pygame.init() 

# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
# left_bound = win_width / 40             # границы, за которые персонаж не выходит (начинает ехать фон)
# right_bound = win_width - left_bound

img_file_back='cave.png'
img_file_hero='m1.png'  # картинка для персонажа
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

# Запуск игры
pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode([win_width, win_height])

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 

# список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# список препятствий:
barriers = pygame.sprite.Group()

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
                robin.x_speed = -5 # персонаж должен пойти налево
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 5 # персонаж должен пойти направо
            elif event.key == pygame.K_UP:
                robin.y_speed = -5 # персонаж должен пойти вверх (ось Y направлена вниз!)
            elif event.key == pygame.K_DOWN:
                robin.y_speed = 5 # персонаж должен пойти вниз

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
    
    pygame.display.update() 

    # Пауза
    timer.tick(FPS)
