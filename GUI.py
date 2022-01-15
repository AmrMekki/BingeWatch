
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont


#initiallize GUI application
widgets = {
      "images" : [],
      "buttons" : []
}
watchApp = QApplication(sys.argv)
grid = QGridLayout()
#window and settings
watchWindow = QWidget()
watchWindow.setWindowTitle("Stay in Theater")
watchWindow.setFixedSize(500,600)
# potatoWindow.move(4000, 200)     #position of the window may vary depending on screen size
watchWindow.setStyleSheet("background: #FFFDD0;")


/