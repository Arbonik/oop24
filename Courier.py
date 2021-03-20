from Settings import cour_speed_random

# Класс курьер, необходим для переноса почты
class Courier:

    # при создании курьера он получает два филиала, из которого нужно унести почту, и в который перенести
    def __init__(self, fromFilial, toFilial):
        self.x = fromFilial.x
        self.y = fromFilial.y
        self.targetX = toFilial.x
        self.targetY = toFilial.y
        self.speed = 120 + cour_speed_random()  # Количество шагов, за которое курьеры проходят расстояние, чем больше, тем дольше идет
        self.inPath = True
        self.stepDo = 0

    # после доставки почты метод для установки новой цели
    def setTarget(self, toFilial):
        self.targetX = toFilial.x
        self.targetY = toFilial.y
        self.inPath = True

    # перемещение курьера на один шаг, вычисляется как
    # (координаты цели - мои координаты) / скорость
    def move(self):
        diffX = (self.targetX - self.x) / self.speed
        diffY = (self.targetY - self.y) / self.speed
        # Считает количество шагов
        self.stepDo += 1
        # если сделано достаточно шагов, сдаем заявки и обнуляем показатели
        if (self.stepDo == self.speed):
            self.inPath = False
            self.x = self.targetX
            self.y = self.targetY
            self.stepDo = 0
    #возвращаем смещение
        return (diffX, diffY)
