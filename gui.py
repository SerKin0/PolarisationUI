# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1242, 700)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_com = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_com.sizePolicy().hasHeightForWidth())
        self.label_com.setSizePolicy(sizePolicy)
        self.label_com.setObjectName("label_com")
        self.horizontalLayout_2.addWidget(self.label_com)
        self.box_com = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_com.sizePolicy().hasHeightForWidth())
        self.box_com.setSizePolicy(sizePolicy)
        self.box_com.setObjectName("box_com")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.horizontalLayout_2.addWidget(self.box_com)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_speed = QtWidgets.QLabel(Dialog)
        self.label_speed.setScaledContents(False)
        self.label_speed.setWordWrap(True)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_4.addWidget(self.label_speed)
        self.speed_box = QtWidgets.QComboBox(Dialog)
        self.speed_box.setObjectName("speed_box")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.speed_box.addItem("")
        self.horizontalLayout_4.addWidget(self.speed_box)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.port_update = QtWidgets.QPushButton(Dialog)
        self.port_update.setObjectName("port_update")
        self.verticalLayout.addWidget(self.port_update)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_angle = QtWidgets.QLabel(Dialog)
        self.label_angle.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_angle.sizePolicy().hasHeightForWidth())
        self.label_angle.setSizePolicy(sizePolicy)
        self.label_angle.setObjectName("label_angle")
        self.horizontalLayout_3.addWidget(self.label_angle)
        self.angle_box = QtWidgets.QSpinBox(Dialog)
        self.angle_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_box.sizePolicy().hasHeightForWidth())
        self.angle_box.setSizePolicy(sizePolicy)
        self.angle_box.setMinimum(-1000000)
        self.angle_box.setMaximum(1000000)
        self.angle_box.setObjectName("angle_box")
        self.horizontalLayout_3.addWidget(self.angle_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setEnabled(False)
        self.dial.setMinimum(-360)
        self.dial.setMaximum(360)
        self.dial.setSingleStep(5)
        self.dial.setPageStep(0)
        self.dial.setProperty("value", 0)
        self.dial.setSliderPosition(0)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.dial)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_speed_rotation = QtWidgets.QLabel(Dialog)
        self.label_speed_rotation.setEnabled(False)
        self.label_speed_rotation.setWordWrap(True)
        self.label_speed_rotation.setObjectName("label_speed_rotation")
        self.horizontalLayout_5.addWidget(self.label_speed_rotation)
        self.speed_rotation_box = QtWidgets.QSpinBox(Dialog)
        self.speed_rotation_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_rotation_box.sizePolicy().hasHeightForWidth())
        self.speed_rotation_box.setSizePolicy(sizePolicy)
        self.speed_rotation_box.setMinimum(2)
        self.speed_rotation_box.setMaximum(20)
        self.speed_rotation_box.setObjectName("speed_rotation_box")
        self.horizontalLayout_5.addWidget(self.speed_rotation_box)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_now_speed = QtWidgets.QLabel(Dialog)
        self.label_now_speed.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_now_speed.sizePolicy().hasHeightForWidth())
        self.label_now_speed.setSizePolicy(sizePolicy)
        self.label_now_speed.setObjectName("label_now_speed")
        self.verticalLayout.addWidget(self.label_now_speed)
        self.label_angle_all = QtWidgets.QLabel(Dialog)
        self.label_angle_all.setEnabled(False)
        self.label_angle_all.setObjectName("label_angle_all")
        self.verticalLayout.addWidget(self.label_angle_all)
        self.zero_button = QtWidgets.QPushButton(Dialog)
        self.zero_button.setEnabled(False)
        self.zero_button.setObjectName("zero_button")
        self.verticalLayout.addWidget(self.zero_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.rotate_button = QtWidgets.QPushButton(Dialog)
        self.rotate_button.setEnabled(False)
        self.rotate_button.setObjectName("rotate_button")
        self.verticalLayout.addWidget(self.rotate_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_cos = QtWidgets.QLabel(Dialog)
        self.label_cos.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cos.sizePolicy().hasHeightForWidth())
        self.label_cos.setSizePolicy(sizePolicy)
        self.label_cos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_cos.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.label_cos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_cos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cos.setObjectName("label_cos")
        self.verticalLayout_2.addWidget(self.label_cos)
        self.button_create_cos = QtWidgets.QPushButton(Dialog)
        self.button_create_cos.setEnabled(False)
        self.button_create_cos.setObjectName("button_create_cos")
        self.verticalLayout_2.addWidget(self.button_create_cos)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_I_0 = QtWidgets.QLabel(Dialog)
        self.label_I_0.setEnabled(False)
        self.label_I_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_I_0.setObjectName("label_I_0")
        self.verticalLayout_3.addWidget(self.label_I_0)
        self.slider_I_0 = QtWidgets.QSlider(Dialog)
        self.slider_I_0.setEnabled(False)
        self.slider_I_0.setMaximum(200)
        self.slider_I_0.setSingleStep(5)
        self.slider_I_0.setOrientation(QtCore.Qt.Horizontal)
        self.slider_I_0.setObjectName("slider_I_0")
        self.verticalLayout_3.addWidget(self.slider_I_0)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_k = QtWidgets.QLabel(Dialog)
        self.label_k.setEnabled(False)
        self.label_k.setAlignment(QtCore.Qt.AlignCenter)
        self.label_k.setObjectName("label_k")
        self.verticalLayout_5.addWidget(self.label_k)
        self.slider_k = QtWidgets.QSlider(Dialog)
        self.slider_k.setEnabled(False)
        self.slider_k.setMinimum(1)
        self.slider_k.setMaximum(700)
        self.slider_k.setSingleStep(10)
        self.slider_k.setOrientation(QtCore.Qt.Horizontal)
        self.slider_k.setObjectName("slider_k")
        self.verticalLayout_5.addWidget(self.slider_k)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_C = QtWidgets.QLabel(Dialog)
        self.label_C.setEnabled(False)
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C.setObjectName("label_C")
        self.verticalLayout_4.addWidget(self.label_C)
        self.slider_C = QtWidgets.QSlider(Dialog)
        self.slider_C.setEnabled(False)
        self.slider_C.setMaximum(300)
        self.slider_C.setSingleStep(10)
        self.slider_C.setOrientation(QtCore.Qt.Horizontal)
        self.slider_C.setObjectName("slider_C")
        self.verticalLayout_4.addWidget(self.slider_C)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_s = QtWidgets.QLabel(Dialog)
        self.label_s.setEnabled(False)
        self.label_s.setAlignment(QtCore.Qt.AlignCenter)
        self.label_s.setObjectName("label_s")
        self.verticalLayout_6.addWidget(self.label_s)
        self.slider_s = QtWidgets.QSlider(Dialog)
        self.slider_s.setEnabled(False)
        self.slider_s.setMinimum(-50)
        self.slider_s.setMaximum(50)
        self.slider_s.setSingleStep(5)
        self.slider_s.setPageStep(1)
        self.slider_s.setOrientation(QtCore.Qt.Horizontal)
        self.slider_s.setObjectName("slider_s")
        self.verticalLayout_6.addWidget(self.slider_s)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_com.setText(_translate("Dialog", "COM-порт"))
        self.box_com.setItemText(0, _translate("Dialog", "COM1"))
        self.box_com.setItemText(1, _translate("Dialog", "COM2"))
        self.box_com.setItemText(2, _translate("Dialog", "COM3"))
        self.box_com.setItemText(3, _translate("Dialog", "COM4"))
        self.box_com.setItemText(4, _translate("Dialog", "COM5"))
        self.box_com.setItemText(5, _translate("Dialog", "COM6"))
        self.box_com.setItemText(6, _translate("Dialog", "COM7"))
        self.box_com.setItemText(7, _translate("Dialog", "COM8"))
        self.box_com.setItemText(8, _translate("Dialog", "COM9"))
        self.box_com.setItemText(9, _translate("Dialog", "COM10"))
        self.label_speed.setText(_translate("Dialog", "Cкорость передачи данных"))
        self.speed_box.setCurrentText(_translate("Dialog", "300"))
        self.speed_box.setItemText(0, _translate("Dialog", "300"))
        self.speed_box.setItemText(1, _translate("Dialog", "600"))
        self.speed_box.setItemText(2, _translate("Dialog", "1200"))
        self.speed_box.setItemText(3, _translate("Dialog", "2400"))
        self.speed_box.setItemText(4, _translate("Dialog", "4800"))
        self.speed_box.setItemText(5, _translate("Dialog", "9600"))
        self.speed_box.setItemText(6, _translate("Dialog", "14400"))
        self.speed_box.setItemText(7, _translate("Dialog", "19200"))
        self.speed_box.setItemText(8, _translate("Dialog", "28800"))
        self.speed_box.setItemText(9, _translate("Dialog", "38400"))
        self.speed_box.setItemText(10, _translate("Dialog", "57600"))
        self.speed_box.setItemText(11, _translate("Dialog", "115200"))
        self.port_update.setText(_translate("Dialog", "Обновить COM-порт"))
        self.label_angle.setText(_translate("Dialog", "Угол"))
        self.label_speed_rotation.setText(_translate("Dialog", "Коэффицент скорости"))
        self.label_now_speed.setText(_translate("Dialog", "Скорость: "))
        self.label_angle_all.setText(_translate("Dialog", "Угол: "))
        self.zero_button.setText(_translate("Dialog", "Обнулить угол"))
        self.rotate_button.setText(_translate("Dialog", "Поворот"))
        self.label_cos.setText(_translate("Dialog", "Уравнение квадратного косинуса (Закон Малюса):     I(φ) = I_0 * cos ^ 2 (φ / k + s) + C"))
        self.button_create_cos.setText(_translate("Dialog", "Построить"))
        self.label_I_0.setText(_translate("Dialog", "I_0: 0"))
        self.label_k.setText(_translate("Dialog", "k: 0"))
        self.label_C.setText(_translate("Dialog", "C: 0"))
        self.label_s.setText(_translate("Dialog", "s: 0"))
