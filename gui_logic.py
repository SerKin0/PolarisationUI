import asyncio
import concurrent.futures
import tracemalloc

import numpy as np
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from arduino_logic import ArduinoController
from gui import Ui_Dialog

reducer = 63.68395
steps_in_the_degree = ((32 * reducer) / 360) / 4 * 3.5
angle = 0
tracemalloc.start()
count_draw_graph = 3
I_0 = 0
k = 1
C = 0
s = 0
# Создаем массив, в который будем записывать измерения с датчика
data = []


def speed(delay_of_steps):
    return 1 / (4 * steps_in_the_degree * delay_of_steps / 1000)


async def run_with_threadpool_executor(func, *args):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await asyncio.get_event_loop().run_in_executor(pool, func, *args)


class GuiProgram(Ui_Dialog, ArduinoController):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        layout = QVBoxLayout()
        # QTWidget
        self.widget.setLayout(layout)
        self.canvas = FigureCanvasQTAgg(Figure())
        # layout.addToolBar(NavigationToolbar(self.canvas, self))
        # QTButton
        self.port_update.clicked.connect(self.connect_arduino)
        self.rotate_button.clicked.connect(self.connect_rotate)
        self.zero_button.clicked.connect(lambda: self.label_angle_all.setText("Угол: 0 град."))
        self.button_create_cos.clicked.connect(self.create_graph_Malusa)
        # QTLabel
        self.label_now_speed.setText(f"Скорость: {speed(self.speed_rotation_box.value()) // 0.0001 / 10000} град./сек.")
        self.label_angle_all.setText(f"Угол: {angle} град.")
        self.label_I_0.setText(f"I_0: {I_0}")
        self.label_k.setText(f"k: {k}")
        self.label_C.setText(f"C: {C}")
        # QTDial
        self.dial.valueChanged.connect(self.on_dial_changed)
        # QTBar
        self.speed_rotation_box.valueChanged.connect(self.on_box_speed_rotation_changed)
        # QTSlider
        self.slider_k.valueChanged.connect(self.changed_k)
        self.slider_C.valueChanged.connect(self.changed_C)
        self.slider_I_0.valueChanged.connect(self.changed_I_0)
        self.slider_s.valueChanged.connect(self.changed_s)

        # Параметры графика в QTWidget
        self.canvas = FigureCanvasQTAgg(Figure())
        layout.addWidget(self.canvas)
        self.fig = self.canvas.figure
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.line_real = None
        self.line_cos = None
        self.ax.set_title("Значения с датчика")
        self.ax.set_xlabel("Измерение")
        self.ax.set_ylabel("Значение, у.е.")

    def changed_I_0(self, value):
        global I_0
        self.label_I_0.setText(f"I_0: {value}")
        I_0 = value
        self.create_graph_Malusa()

    def changed_C(self, value):
        global C
        self.label_C.setText(f"C: {value}")
        C = value
        self.create_graph_Malusa()

    def changed_k(self, value):
        global k
        self.label_k.setText(f"k: {value}")
        k = value
        self.create_graph_Malusa()

    def changed_s(self, value):
        global s
        self.label_s.setText(f"s: {value}")
        s = value
        self.create_graph_Malusa()

    def create_graph_Malusa(self):
        if data:
            x = np.arange(len(data))
            y = np.real(I_0 * np.cos(x / k + (s / 10)) ** 2 + C)

            if self.line_cos:
                self.line_cos.set_ydata(y)
            else:
                self.line_cos, = self.ax.plot(x, y, color='red', label='Теоретический график')
                self.ax.legend()

            self.canvas.draw()

    async def create_graph(self):
        # Очищаем виджет, в котором будем рисовать график
        self.ax.clear()
        # Устанавливаем значения угла по оси X
        # ...
        # Устанавливаем название осей и самого графика
        self.ax.set_title("Значения с датчика")
        self.ax.set_xlabel("Измерение")
        self.ax.set_ylabel("Значение, у.е.")
        # Создаем график
        self.ax.plot(data, color='blue', label='Реальный график')
        # Рисуем график
        self.canvas.draw()

    # сли мы поворачиваем QTDial (крутилку), то...
    def on_dial_changed(self, value):
        print(f"QDial: {value}")  # Обновление данных в приложении
        # Изменяем значения QTBar с коэффициентами скорости
        self.angle_box.setValue(value)

    # Если мы изменяем значения в QTBar с коэффициентом скорости поворота, то...
    def on_box_speed_rotation_changed(self, value):
        # Изменяем значения в текстовом виджете со значением скорости поворота
        self.label_now_speed.setText(f"Скорость: {speed(value) // 0.0001 / 10000} град./сек.")

    # Действие, при нажатии кнопки подключения к Arduino
    def connect_arduino(self):
        # Записываем Serial-порт и скорость передачи данных в переменные в классе Arduino
        ArduinoController.serial_port = self.box_com.currentText()
        ArduinoController.baud_rate = int(self.speed_box.currentText())
        # Если мы смогли подключиться к Arduino, то делаем доступными для пользователя виджеты для поворота системы
        if ArduinoController.connect(self):
            self.switch_enabled()

    def connect_rotate(self):
        # Подключаем глобальную переменную хранящую угол относительно нулевого угла
        global angle, data
        # Выставляем прогресс-бар в нулевое положение
        self.progressBar.setValue(0)
        # Отправляем команду на Arduino, которая запускает поворот на некий угол с определенной скоростью
        ArduinoController.send_data(self, f"{self.angle_box.value()}\n{self.speed_rotation_box.value()}\n")
        data = []
        # Переменная для подсчета количества выполненных измерений
        count = 0
        # Записываем в переменную входные данные из консоли Arduino
        tmp = ArduinoController.receive_data(self)
        # Читаем консоль до момента, когда не подойдет конец, то есть не выведется символ "е"
        while "e" not in tmp:
            count += 1
            # Добавляем новое измерение с датчика
            data.append(float(tmp))
            # Обновляем прогресс-бар
            self.progressBar.setValue(int(count * 100 / (steps_in_the_degree * abs(self.angle_box.value()))))
            # Записываем следующие значение измерения
            tmp = ArduinoController.receive_data(self)
            if count % int(steps_in_the_degree * self.angle_box.value() / count_draw_graph) == 0:
                asyncio.run(self.create_graph())

        print(data)
        # Выводим график значений измерений от угла поворота
        asyncio.run(self.create_graph())
        # Обновляем значение абсолютного угла поворота
        angle += self.angle_box.value()
        # Изменяем значение абсолютного в приложении
        self.label_angle_all.setText(f"Угол: {angle} град.")

    # Делает недоступными для редактирования элементы после подключения к Arduino, которые отвечают за подключение.
    # И делает активными те, которые управляют поворотом.
    def switch_enabled(self):
        # Записываем все элементы, которые должны будут менять режимы доступности в массив
        widgets = [
            self.angle_box, self.label_com, self.label_angle, self.dial,
            self.rotate_button, self.box_com, self.speed_box,
            self.label_speed, self.label_speed_rotation, self.speed_rotation_box,
            self.label_now_speed, self.progressBar, self.label_angle_all, self.zero_button,
            self.label_I_0, self.label_C, self.label_k, self.slider_I_0, self.slider_C, self.slider_k,
            self.label_cos, self.button_create_cos, self.label_s, self.slider_s
        ]
        # Перебираем каждый элемент (виджет) и меняем его состояние
        for widget in widgets:
            widget.setEnabled(not widget.isEnabled())
