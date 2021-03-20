
class Request:
    # заявка имеет место старта и окончания
    def __init__(self, fromFilial, toFilial):
        self.fromFilial = fromFilial
        self.toFilial = toFilial

    # возвращает пару место отправления - место прибытия
    def getRequest(self):
        return (self.fromFilial, self.toFilial)