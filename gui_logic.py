from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ard import ArduinoController
from gui import Ui_Dialog

reducer = 63.68395
steps_in_the_degree = ((32 * reducer) / 360) / 4 * 3.5
print(f"steps_in_the_degree = {steps_in_the_degree}")
angle = 0


def speed(delay_of_steps):
    return 1 / (4 * steps_in_the_degree * delay_of_steps / 1000)


def on_box_angle_changed(value):
    print(f"QBox: {value}")


class GuiProgram(Ui_Dialog, ArduinoController):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.port_update.clicked.connect(self.connect_arduino)
        self.dial.valueChanged.connect(self.on_dial_changed)
        self.angle_box.valueChanged.connect(on_box_angle_changed)
        self.speed_rotation_box.valueChanged.connect(self.on_box_speed_rotation_changed)
        self.rotate_button.clicked.connect(self.connect_rotate)
        self.label_now_speed.setText(f"Скорость: {speed(self.speed_rotation_box.value()) // 0.0001 / 10000} град./сек.")
        self.label_angle_all.setText(f"Скорость: {angle} град.")
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.canvas = FigureCanvasQTAgg(Figure())
        layout.addWidget(self.canvas)

    def create_graph(self, mass, start_angle, end_angle):
        fig = self.canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        ax.set_xlim(start_angle, end_angle)
        title = "Значения с датчика"
        ax.set_title(title)
        ax.set_xlabel("Измерение")
        ax.set_ylabel("Значение, у.е.")
        im = ax.plot(list(range(len(mass))), mass)
        self.canvas.draw()

    def on_dial_changed(self, value):
        print(f"QDial: {value}")  # Обновление данных в твоем приложении
        self.angle_box.setValue(value)

    def on_box_speed_rotation_changed(self, value):
        self.label_now_speed.setText(f"Скорость: {speed(value) // 0.0001 / 10000} град./сек.")

    def connect_arduino(self):
        ArduinoController.serial_port = self.box_com.currentText()
        ArduinoController.baud_rate = int(self.speed_box.currentText())
        print(ArduinoController.serial_port, ArduinoController.baud_rate)
        if ArduinoController.connect(self):
            self.switch_enabled()

    def connect_rotate(self):
        global angle
        self.progressBar.setValue(0)
        ArduinoController.send_data(self, f"{self.angle_box.value()}\n")
        ArduinoController.send_data(self, f"{self.speed_rotation_box.value()}\n")
        mass = []
        count = 0
        tmp = ArduinoController.receive_data(self)
        while "e" not in tmp:
            count += 1
            mass.append(float(tmp))
            print(int(count * 100 / (steps_in_the_degree * abs(self.angle_box.value()))))
            self.progressBar.setValue(int(count * 100 / (steps_in_the_degree * abs(self.angle_box.value()))))
            tmp = ArduinoController.receive_data(self)

        print(f"count = {count}")

        print(mass, min(angle, angle + self.angle_box.value()), max(angle, angle + self.angle_box.value()))
        self.create_graph(mass, angle, angle + self.angle_box.value())
        mass = []
        angle += self.angle_box.value()
        self.label_angle_all.setText(f"Скорость: {angle} град.")

    def switch_enabled(self):
        self.angle_box.setEnabled(False if self.angle_box.isEnabled() else True)
        self.label_com.setEnabled(False if self.label_com.isEnabled() else True)
        self.label_angle.setEnabled(False if self.label_angle.isEnabled() else True)
        self.dial.setEnabled(False if self.dial.isEnabled() else True)
        self.rotate_button.setEnabled(False if self.rotate_button.isEnabled() else True)
        self.box_com.setEnabled(False if self.box_com.isEnabled() else True)
        self.speed_box.setEnabled(False if self.speed_box.isEnabled() else True)
        self.label_speed.setEnabled(False if self.label_speed.isEnabled() else True)
        self.label_speed_rotation.setEnabled(False if self.label_speed_rotation.isEnabled() else True)
        self.speed_rotation_box.setEnabled(False if self.speed_rotation_box.isEnabled() else True)
        self.label_now_speed.setEnabled(False if self.label_now_speed.isEnabled() else True)
        self.progressBar.setEnabled(False if self.progressBar.isEnabled() else True)
        self.label_angle_all.setEnabled(False if self.label_angle_all.isEnabled() else True)
