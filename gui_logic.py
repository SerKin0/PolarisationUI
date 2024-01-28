import asyncio
import concurrent.futures

import numpy as np
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from arduino_logic import ArduinoController
from gui import Ui_Dialog

steps_in_the_degree = ((32 * 63.68395) / 360) / 4 * 3.5
count_draw_graph = 3

def speed(delay_of_steps: int) -> float:
    """Calculates the speed of rotation of the step engine in (deg/sec)

    Args:
        delay_of_steps (int): The delay between the turn

    Returns:
        float: Turning speed in hail/sec.
    """
    return 1 / (4 * steps_in_the_degree * delay_of_steps / 1000)


class GuiProgram(Ui_Dialog, ArduinoController):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        layout = QVBoxLayout()
        
        # Параметры / Переменные
        self.I_0 = 0
        self.k = 1
        self.C = 0
        self.s = 0
        self.data = []  # Array with measurements from the sensor
        self.angle = 0  # The total angle of rotation

        # QTWidget
        self.widget.setLayout(layout)
        self.canvas = FigureCanvasQTAgg(Figure())
        # QTButton
        self.port_update.clicked.connect(self.connect_arduino)
        self.rotate_button.clicked.connect(self.connect_rotate)
        self.zero_button.clicked.connect(lambda: self.label_angle_all.setText("Угол: 0 град."))
        self.button_create_cos.clicked.connect(self.create_graph_Malusa)
        # QTLabel
        self.label_now_speed.setText(f"Скорость: {speed(self.speed_rotation_box.value()) // 0.0001 / 10000} град./сек.")
        self.label_angle_all.setText(f"Угол: {self.angle} град.")
        self.label_I_0.setText(f"I_0: {self.I_0}")
        self.label_k.setText(f"k: {self.k}")
        self.label_C.setText(f"C: {self.C}")
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

    def changed_I_0(self, value: int) -> None:
        """Changing the amplitude intensity parameter (I_0)

        Args:
            value (int): Value from the widget
        """
        self.label_I_0.setText(f"I_0: {value}")
        self.I_0 = value
        self.create_graph_Malusa()

    def changed_C(self, value: int) -> None:
        """Changing the parameter for adjusting the theoretical graph on the Y axis (С)

        Args:
            value (int): Value from the widget
        """
        self.label_C.setText(f"C: {value}")
        self.C = value
        self.create_graph_Malusa()

    def changed_k(self, value: int) -> None:
        """Changing the parameter of the oscillation period (k)

        Args:
            value (int): Value from the widget
        """
        self.label_k.setText(f"k: {value}")
        self.k = value
        self.create_graph_Malusa()

    def changed_s(self, value: int) -> None:
        """Changing the parameter for displacement along the X (s) axis

        Args:
            value (int): Values from the widget
        """
        self.label_s.setText(f"s: {value}")
        self.s = value
        self.create_graph_Malusa()

    def create_graph_Malusa(self) -> None:
        """ Bringing the theoretical graph on the equation of Malyus """
        if self.data:
            x = np.arange(len(self.data))
            y = np.real(self.I_0 * np.cos(x / self.k + (self.s / 10)) ** 2 + self.C)

            if self.line_cos:
                self.line_cos.set_ydata(y)
            else:
                self.line_cos, = self.ax.plot(x, y, color='red', label='Теоретический график')
                self.ax.legend()

            self.canvas.draw()

    async def create_graph(self) -> None:
        """ Draw a data schedule from the sensor"""
        # Очищаем виджет, в котором будем рисовать график
        self.ax.clear()
        # Устанавливаем название осей и самого графика
        self.ax.set_title("Значения с датчика")
        self.ax.set_xlabel("Измерение")
        self.ax.set_ylabel("Значение, у.е.")
        # Создаем график
        self.ax.plot(self.data, color='blue', label='Реальный график')
        # Рисуем график
        self.canvas.draw()

    # Если мы поворачиваем QTDial (крутилку), то...
    def on_dial_changed(self, value: int) -> None:

        print(f"QDial: {value}")  # Обновление данных в приложении
        # Изменяем значения QTBar с коэффициентами скорости
        self.angle_box.setValue(value)

    # Если мы изменяем значения в QTBar с коэффициентом скорости поворота, то...
    def on_box_speed_rotation_changed(self, value):
        # Изменяем значения в текстовом виджете со значением скорости поворота
        self.label_now_speed.setText(f"Скорость: {speed(value) // 0.0001 / 10000} град./сек.")

    def connect_arduino(self) -> None:
        """Действие, при нажатии кнопки подключения к Arduino """
        # Записываем Serial-порт и скорость передачи данных в переменные в классе Arduino
        ArduinoController.serial_port = self.box_com.currentText()
        ArduinoController.baud_rate = int(self.speed_box.currentText())
        # Если мы смогли подключиться к Arduino, то делаем доступными для пользователя виджеты для поворота системы
        if ArduinoController.connect(self):
            self.switch_enabled()

    def connect_rotate(self):
        # Выставляем прогресс-бар в нулевое положение
        self.progressBar.setValue(0)
        # Отправляем команду на Arduino, которая запускает поворот на некий угол с определенной скоростью
        ArduinoController.send_data(self, f"{self.angle_box.value()}\n{self.speed_rotation_box.value()}\n")
        self.data = []
        # Переменная для подсчета количества выполненных измерений
        count = 0
        # Записываем в переменную входные данные из консоли Arduino
        tmp = ArduinoController.receive_data(self)
        # Читаем консоль до момента, когда не подойдет конец, то есть не выведется символ "е"
        while "e" not in tmp:
            count += 1
            # Добавляем новое измерение с датчика
            self.data.append(float(tmp))
            # Обновляем прогресс-бар
            self.progressBar.setValue(int(count * 100 / (steps_in_the_degree * abs(self.angle_box.value()))))
            # Записываем следующие значение измерения
            tmp = ArduinoController.receive_data(self)
            if count % int(steps_in_the_degree * self.angle_box.value() / count_draw_graph) == 0:
                asyncio.run(self.create_graph())

        print(self.data)
        # Выводим график значений измерений от угла поворота
        asyncio.run(self.create_graph())
        # Обновляем значение абсолютного угла поворота
        self.angle += self.angle_box.value()
        # Изменяем значение абсолютного в приложении
        self.label_angle_all.setText(f"Угол: {self.angle} град.")

    def switch_enabled(self) -> None:
        """After connecting to the Arduino board, the connection buttons become inaccessible to rarefaction, and measurement widgets, on the contrary
        """
        # We write down all the elements that will have to change accessories in the array
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
