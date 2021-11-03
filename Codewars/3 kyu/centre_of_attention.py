class CentralPixelsFinder:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h

    def central_pixels(self, colour):
        # Запомним длину нашего массива:
        length = self.width * self.height
        # Создадим два списка для индексов наших пикселей и переменную - максимальную глубину
        cur_depth, next_depth = [], []
        # Переберём весь список пикселей
        for pixel_index in range(length):
            # Если наш пиксель искомого цвета, то сначала присвоим его глубине значение 1
            if self.pixels[pixel_index] == colour:
                cur_depth.append(pixel_index)

        for pixel_index in cur_depth:
            if (pixel_index - 1 in cur_depth) and (pixel_index + 1 in cur_depth) and \
               (pixel_index - self.width in cur_depth) and (pixel_index + self.width in cur_depth):
                next_depth.append(pixel_index)

        while len(next_depth) != 0:
            cur_depth, next_depth = next_depth, []
            for pixel_index in cur_depth:
                if (pixel_index - 1 in cur_depth) and (pixel_index + 1 in cur_depth) and \
                        (pixel_index - self.width in cur_depth) and (pixel_index + self.width in cur_depth):
                    next_depth.append(pixel_index)

        return cur_depth


image = CentralPixelsFinder([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
                             1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                             1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                             1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
                             1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
                             1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)

image.pixels[32] = 3
print(image.central_pixels(1))
