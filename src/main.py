import sys
from PySide6.QtWidgets import QApplication
from ui import DataManagementApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataManagementApp()
    window.show()
    app.exec()