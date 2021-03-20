import random


# Настройки модели
N = random.randint(3, 7)  # количество филиалов
M = random.randint(1, 5)  # количество курьеров


time_start = 8 # время старта моделирования
time_finish = 20 # время окончания моделирования
time_step =0.3  # 0.5 - 30 минут
days = 100 # количество дней моделирования

# Частота заявок
cooldown = 20

# отклонение скорости курьера
def cour_speed_random():
    return random.randint(-20, 40)

