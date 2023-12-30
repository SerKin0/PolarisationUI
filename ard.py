import serial
from PyQt5.QtWidgets import QMessageBox


class ArduinoController:
    def __init__(self, serial_port, baud_rate):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.ser = None

    def connect(self):
        try:
            # self.disconnect()
            # Устанавливаем соединение с Arduino
            self.ser = serial.Serial(self.serial_port, self.baud_rate)
            print(f"p = {self.ser.isOpen()}")
            print(f"Успешно подключено к {self.serial_port} на скорости {self.baud_rate}")
            return True
        except serial.SerialException:
            QMessageBox.warning(None, "Порт не найден",
                                "Ошибка подключения. Проверьте порт и скорость передачи данных.")
            print("Ошибка подключения. Проверьте порт и скорость передачи данных.")
            return False

    def disconnect(self):
        if not self.ser.isOpen():
            self.ser.close()
            print("Соединение с Arduino разорвано.")
        else:
            print("Нет активного соединения для разрыва.")

    def send_data(self, data):
        if self.ser:
            self.ser.write(data.encode('utf-8'))
            print(f"Данные отправлены на Arduino: {data}")
        else:
            print("Нет активного соединения для отправки данных.")

    def receive_data(self):
        if self.ser:
            incoming_data = self.ser.readline()
            print(f"Получены данные от Arduino: {incoming_data.decode('utf-8').strip()}")
            return incoming_data.decode('utf-8').strip()
        else:
            print("Нет активного соединения для получения данных.")
