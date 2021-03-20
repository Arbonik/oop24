from Courier import Courier
from Filial import generateFilial

class Dispatcher():

    def __init__(self, N, M):
        # все заявки
        self.requests = []
        # все созданные заявки
        self.allCountRequestes = 0
        # все успешно
        self.successCountRequestes = 0
        # создание филиалов
        self.filials = [generateFilial() for i in range(N)]
        # создание курьеров
        self.couriers = [self._createCourier() for i in range(M)]


    def createRequest(self):
        #имитация do - while, чтобы была создана как минимум одна заявка
        while (True):
            for filial in self.filials:

                result = filial.generateRequest(self.filials)
                if result is not None:
                    self.allCountRequestes += 1
                    self.requests.append(result)

            if (len(self.requests) != 0):
                break
        # курьер берет первую заявку
        a = self.requests[0]
        self.requests.remove(a)
        return a.getRequest()

    def _createCourier(self):
        # создание первой заявки для курьера
        d = self.createRequest()
        cour = Courier(d[0], d[1])
        return cour

    def step(self):
        # массив для хранения смещения всех курьеров
        ret = []
        for i in range(0, len(self.couriers) - 1):
            # Рассчет расстояния на перемещение
            diff = self.couriers[i].move()

        # если курьер доставил заявку, даем другую
            if not self.couriers[i].inPath:
                self.successCountRequestes += 1
                self.couriers[i].setTarget(self.createRequest()[1])
            ret.append(diff)

        return ret
