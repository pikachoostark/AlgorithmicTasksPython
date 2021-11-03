# Подключим нужные модули
import pygame  # в программе появляется пространство имён pygame,

# внутри которого находятся все идентификаторы из модуля
pygame.init()  # функция инициализации подключает дополнительные возможности и настраивает библиотеку

# Глобальные переменные (настройки)
win_width = 800
win_height = 600
left_bound = win_width / 40  # граница, за которую персонаж не выходит (начинает ехать фон)
right_bound = win_width - left_bound  #

img_file_back = "cave.png"
img_file_hero = "m1.png"  # картинка персонажа
img_file_enemy = "enemy.png"  # картинка для врага
FPS = 60  # будем повторять цикл FPS раз в секунду
shift = 0  # сдвиг фона
speed = 0  # текущая скорость движения

C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)


# Запуск
# Класс нашего персонажа
class Hero(pygame.sprite.Sprite):
    """ Класс для героя игры - наследник класса Sprite """

    def __init__(self, filename, x_speed=0, y_speed=0, x=left_bound, y=0, width=120, height=120):
        """ Конструктор класса.
            Берёт картинку персонажа из файла, устанавливает в нужной точке. """
        pygame.sprite.Sprite.__init__(self)  # вызываем конструктор базового класса Sprite
        # это НЕ РАБОТАЕТ! через super(), приходится писать сам класс Sprite
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
        # каждый спрайт должен иметь свойство image - картинка (Surface)
        # картинка загружается из файла и уменьшается в прямоугольник нужных размеров
        # используем .convert_alpha(), чтобы сохранить прозрачность.

        self.rect = self.image.get_rect()
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect.x = x
        self.rect.y = y
        # ставим персонажа в определённую точку (x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
        # создаём дополнительные свойства, запоминаем переданные значения

    def update(self):
        """ Перемещает персонажа, используя вертикальную и горизонтальную скорость. """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


class Wall(pygame.sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        pygame.sprite.Sprite.__init__(self)
        # Картинка - новый прямоугольник нужных размеров
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Создаём свойство Rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


timer = pygame.time.Clock()  # объект timer нужен для того, чтобы запускать основной цикл с паузами

window = pygame.display.set_mode([win_width, win_height])  # создание окна указанных размеров
# (в остальном графический режим - по умолчанию)
pygame.display.set_caption("ARCADE")  # установка надписи окна программы
# (устанавливать в любой момент, даже до создания окна)

img1 = pygame.image.load(img_file_back)  # загрузка картинки из файла
img2 = img1.convert()  # формат картинки img2 - тот же, что у экранной поверхности
back = pygame.transform.scale(img2, (win_width, win_height))  # размеры картинки back - те же, что у окна

# ПЕРЕНЕСЛИ ЭТИ СТРОКИ В ОСнОВНЕОЙ ЦИКЛ ИГРЫ
# window.blit(back, (0, 0))  # экранная поверхность поменялась в памяти
# pygame.display.update()   # обновилось содержимое окна, теперь видно последнее состояние экранной поверхности

# Список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# Список всех стен:
barriers = pygame.sprite.Group()

# Создаём персонажа, добавляем его в список всех спрайтов:
robin = Hero(img_file_hero)
all_sprites.add(robin)

# Создаём стены, добавляем их:
w = Wall(50, 150, 480, 50)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360)
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 400, 640, 50)
barriers.add(w)
all_sprites.add(w)

# Основной цикл игры
run = True  # флаг продолжения программы
while run:
    # Получение событий
    events = pygame.event.get()  # Получили очередь событий (она очистилась!), загрузили полученный список в
    # переменную events
    for event in events:  # проходим по списку
        if event.type == pygame.QUIT:  # тип события QUIT, т.е. человек нажал на крестик закрытия программы
            run = False  # сбрасываем флаг продолжения, цикл больше не повторится, программа закроется
        elif event.type == pygame.KEYDOWN:  # если событие типа "нажата клавиша"
            if event.key == pygame.K_LEFT:  # если это стрелка влево:
                robin.x_speed = -5  # начали движение налево
            elif event.key == pygame.K_RIGHT:  # если это стрелка вправо:
                robin.x_speed = 5  # начали движение направо
            elif event.key == pygame.K_UP:  # если это стрелка вверх:
                robin.y_speed = -5  # начали движение вверх (ось y направлена вниз!)
            elif event.key == pygame.K_DOWN:  # если это стрелка вниз:
                robin.y_speed = 5  # начали движение вниз
        elif event.type == pygame.KEYUP:  # если событие типа "нажата клавиша"
            if event.key == pygame.K_LEFT:  # если это стрелка влево:
                robin.x_speed = 0  # закончили движение
            elif event.key == pygame.K_RIGHT:  # если это стрелка вправо:
                robin.x_speed = 0  # закончили движение
            elif event.key == pygame.K_UP:  # если это стрелка вверх
                robin.y_speed = 0  # закончили движение
            elif event.key == pygame.K_DOWN:  # если это стрелка вниз:
                robin.y_speed = 0  # закончили движение

    # Вычисления:
    #   перемещение игровых объектов
    all_sprites.update()  # обновим все спрайты

    # shift += speed
    # local_shift = shift % win_width  # общий сдвиг может быть несколько экранов
    # # берём остаток от деления на ширину экрана, чтобы получить сдвиг
    # # в пределах экрана и понять, насколько нужно двигать картинку.
    # #   обработка столкновений
    # # проверка по оси Y
    # if robin.rect.top < 0 or robin.rect.bottom > win_height:
    #     robin.rect.y -= robin.y_speed  # запрещаем персонажу выходить вверх и вниз
    # # проверка по оси X
    # if (robin.rect.right > right_bound and robin.x_speed > 0) or \
    #         (robin.rect.left < left_bound and robin.x_speed < 0):
    #     # при выходе вправо или влево персонажем переносим изменение в сдвиг экрана
    #     shift -= robin.x_speed
    #     robin.rect.x -= robin.x_speed
    #
    # #   изменение состояния игры
    # window.blit(back, (local_shift, 0))  # рисуем фон справа от сдвига
    # if local_shift != 0:
    #     window.blit(back, (local_shift - win_width, 0))  # рисуем такой же фон слева от сдвига

    # УБРАЛИ, ТАК КАК ТЕПЕРЬ ДВИГАЕМ ЭКРАН
    window.blit(back, (0, 0))  # в цикле каждый раз будем обновлять картинку
    # Отрисовка
    all_sprites.draw(window)
    pygame.display.update()

    # Пауза
    timer.tick(FPS)  # делает тик.
    # можно заменить функцией pygame.time.delay(ms), но она занимает больше процессорного времени.
