import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout, QLabel
from main import convert_file

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.openButton = QPushButton('Open Input File', self)
        self.openButton.clicked.connect(self.showDialog)
        self.layout.addWidget(self.openButton)

        self.label = QLabel('No file selected', self)
        self.layout.addWidget(self.label)

        self.convertButton = QPushButton('Convert', self)
        self.convertButton.clicked.connect(self.convertFile)
        self.layout.addWidget(self.convertButton)

        self.setLayout(self.layout)

    def showDialog(self):
        self.inputFile, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.label.setText(self.inputFile)

    def convertFile(self):
        outputFile, _ = QFileDialog.getSaveFileName(self, 'Save file', '/home')
        convert_file(self.inputFile, outputFile)

app = QApplication(sys.argv)
ex = ConverterUI()
ex.show()
sys.exit(app.exec_())