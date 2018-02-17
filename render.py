from crowdSimulator.Qt import QtWidgets


def build_gui(window_args=None):
    window_args = window_args or []
    app = QtWidgets.QApplication(window_args)
    button = QtWidgets.QPushButton("Hello World")
    button.show()
    app.exec_()
