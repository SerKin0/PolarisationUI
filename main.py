import asyncio
import sys
from PyQt5 import QtWidgets

import gui_logic
from gui_logic import GuiProgram

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    program = GuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())
