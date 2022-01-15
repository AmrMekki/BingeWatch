import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir

class DialogApp(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 600)
        
        

		self.button1 = QPushButton('Upload a movie poster')
		self.button1.clicked.connect(self.get_image_file)


		self.labelImage = QLabel()
		self.textEditor = QTextEdit()

		layout = QVBoxLayout()
		layout.addWidget(self.button1)
		layout.addWidget(self.labelImage)
		layout.addWidget(self.textEditor)
		self.setLayout(layout)

	def get_image_file(self):
		file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
		self.labelImage.setPixmap(QPixmap(file_name))

	

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = DialogApp()
	demo.show()

	sys.exit(app.exec_())