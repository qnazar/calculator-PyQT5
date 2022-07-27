from PyQt5.QtWidgets import QMainWindow, QToolBar
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class MainUI(QMainWindow):
    def __init__(self, calc_ctrl, conv_ctrl, engine_ctrl):
        """Initializing all main view configs"""
        super(MainUI, self).__init__()
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QtGui.QIcon('static/icon.png'))
        self.setFixedSize(300, 320)
        self.create_tool_bar()

        self.calc_ctrl = calc_ctrl
        self.conv_ctrl = conv_ctrl
        self.engine_ctrl = engine_ctrl
        self.switch_to_calculator()

    def create_tool_bar(self):
        """Creating main toolbar to switch between widgets"""
        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

    def switch_to_calculator(self):
        self.current = self.calc_ctrl()
        self.setFixedSize(300, 320)
        self.setCentralWidget(self.current.initUI())

    def switch_to_converter(self, mode='temp'):
        self.current = self.conv_ctrl(self)
        self.setFixedSize(300, 320)
        self.setCentralWidget(self.current.initUI(mode))

    def switch_to_engine(self):
        self.current = self.engine_ctrl()
        self.setFixedSize(300, 420)
        self.setCentralWidget(self.current.initUI())

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Escape:
            self.centralWidget().close()
        elif e.key() == Qt.Key_F1:
            self.switch_to_calculator()
        elif e.key() == Qt.Key_F2:
            self.switch_to_engine()
        elif e.key() == Qt.Key_F3:
            self.switch_to_converter()


class ToolBar(QToolBar):
    def __init__(self, parent: MainUI):
        super(ToolBar, self).__init__()
        self.create_buttons(parent)

    def create_buttons(self, parent):
        self.addAction('Calculator', parent.switch_to_calculator)
        self.addAction('Engineering', parent.switch_to_engine)
        self.addAction('Converter', parent.switch_to_converter)
        self.addAction('Exit', parent.close)
