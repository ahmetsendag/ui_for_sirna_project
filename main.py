from arayuz import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication,QFormLayout,QPushButton
from PySide6.QtGui import QFont
import sys
import qdarkstyle

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

   
app = QApplication(sys.argv)
window = Main()
window.setFont(QFont("Times",16))
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
window.show()
app.exec()




