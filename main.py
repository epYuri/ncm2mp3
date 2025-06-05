# main.py
import sys
import os
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

def handle_exception(exc_type, exc_value, exc_traceback):
    from PyQt5.QtWidgets import QMessageBox
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    sys.excepthook = handle_exception
    msg.setText("程序发生错误")
    msg.setInformativeText(str(exc_value))
    msg.setWindowTitle("错误")
    msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
