import tkinter as tk

from Dispather import Dispatcher
from Settings import N, M, time_start, time_finish, time_step, days


# смещение координат на центр экрана
def coordTransform(value):
    return value + window_size / 2

# параметры графики
window_size = 1000
filial_size = window_size * 0.005

root = tk.Tk()
c = tk.Canvas(root, width=window_size, height=window_size, bg='white')
c.pack()

dispatcher = Dispatcher(N, M)

for filial in dispatcher.filials:
    #отрисовка филиалов
    c.create_oval(coordTransform(filial.x) - filial_size, coordTransform(filial.y) - filial_size,
                  coordTransform(filial.x) + filial_size, coordTransform(filial.y) + filial_size,
                  width=window_size * 0.01)
    #отрисовка курьеров
    couriersView = [
        c.create_oval(coordTransform(courier.x) - 5, coordTransform(courier.y) - 5, coordTransform(courier.x) + 5,
                      coordTransform(courier.y) + 5) for courier in dispatcher.couriers]

currentDays = 0
#один день
def update():
    current_time = time_start
    while current_time < time_finish:
        # перемещение всех курьеров на пройденное за шаг расстояние
        for diff in enumerate(dispatcher.step()):
            c.move(couriersView[diff[0]], diff[1][0], diff[1][1])
            if not dispatcher.couriers[diff[0]].inPath:
                c.itemconfig(couriersView[diff[0]], fill = "green")
            else:
                c.itemconfig(couriersView[diff[0]], fill = "red")
        current_time += time_step

    global currentDays
    currentDays += 1
    # если моделирование не законченно то вызываем функцию еще раз, иначе заканчиваем
    if currentDays <= days:
        root.after(200, update)
    else:
        print("Обработано заявок: ", dispatcher.successCountRequestes)
        print("Всего заявок: ", dispatcher.allCountRequestes)
        root.destroy()


root.after(200, update)
root.mainloop()