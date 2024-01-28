import serial
from PyQt5.QtWidgets import QMessageBox


class ArduinoController:
    def __init__(self, serial_port, baud_rate):
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.ser = None

    def connect(self) -> bool:
        """Connection of the ARDUINO board

        Returns:
            bool: Returns the connection status
        """
        try:
            # Устанавливаем соединение с Arduino
            self.ser = serial.Serial(self.serial_port, self.baud_rate)
            print(f"Successfully connected to {self.serial_port} at speed {self.baud_rate}")

            return True
        except serial.SerialException:
            QMessageBox.warning(None, "Порт не найден",
                                "Ошибка подключения. Проверьте порт и скорость передачи данных.")
            print("Connection error.Check the port and data transfer speed.")

            return False

    def disconnect(self):
        if not self.ser.isOpen():
            self.ser.close()
            print("The connection with Arduino is torn.")
        else:
            print("There is no active connection for the gap.")

    def send_data(self, data):
        if self.ser:
            self.ser.write(data.encode('utf-8'))
            print(f"Данные отправлены на Arduino: {data}")
        else:
            print("Нет активного соединения для отправки данных.")

    def receive_data(self):
        if self.ser:
            incoming_data = self.ser.readline()
            # print(f"Получены данные от Arduino: {incoming_data.decode('utf-8').strip()}")
            return incoming_data.decode('utf-8').strip()
        else:
            print("Нет активного соединения для получения данных.")
