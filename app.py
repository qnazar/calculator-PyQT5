from PyQt5.QtWidgets import QApplication
from main_view import MainUI

from calculator.controller import CalcController
from converter.controller import ConvController

from static.style import style

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style)

    view = MainUI(CalcController, ConvController)
    view.show()

    app.exec()
