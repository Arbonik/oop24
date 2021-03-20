import random
from math import sqrt

from Request import Request
from Settings import cooldown


class Filial:

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.cd = 0  # кулдаун заявки
        self.requests = []


    def generateRequest(self, filials):
        # если филиал уже может создать заявку
        if (self.cd == 0):
            # фильтрация филиалов, исключение собственного и выбор случайного другого для отправки
            toFilial = random.choice([filial for filial in filials if filial is not self])
            self.requests.append(Request(self, toFilial))
            self.cd = cooldown
            a = self.requests[0]
            self.requests.remove(a)
            return a
        else:
            self.cd -= 1
            return None


def generateFilial():
    # генерация местоположения филиала
    x = random.randint(-100, 100) / 100
    y = sqrt(1 - x * x) * (-1, 1)[random.randint(0, 1)]
    return Filial(x * 100, y * 100)
