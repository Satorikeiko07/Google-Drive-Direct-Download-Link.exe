import sys, io
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, \
                            QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.Qt import Qt, QSize, QFont
from PyQt5.QtGui import QIcon

# Google Drive Direct Download Link Generator

class GeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 380)
        self.setWindowTitle('Google Drive Direct Link Generator')
        self.setWindowIcon(QIcon(r''))
        fnt = QFont('', 13)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # layout.setContentsMargins(left, top, right, bottom)
        layout.setContentsMargins(25, 30, 25, 0)
        layout.setSpacing(15)

        layout.addWidget(QLabel('<font size="5">Enter your sharing URL:</font>'))

        self.EnterURL = QLineEdit()
        self.EnterURL.setFixedSize(QSize(self.width() - 5, 50))
        self.EnterURL.setFont(fnt)
        layout.addWidget(self.EnterURL)

        self.button = QPushButton('Create Direct Link')
        self.button.setFixedSize(250, 50)
        self.button.clicked.connect(self.convert_URL)
        self.setStyleSheet('''
            QPushButton{font-size:26px;font-family: Arial;color:rgb(0, 0, 0);background-color:rgb(233,233,233);}
            ''')
        layout.addWidget(self.button)

        # add space
        layout.addSpacing(25)

        layout.addWidget(QLabel('<font size="5">Output link</font>'))

        self.OutputLink = QLineEdit()
        self.OutputLink.setFixedSize(QSize(self.width() - 5, 50))
        self.OutputLink.setFont(fnt)
        self.OutputLink.setReadOnly(True)
        layout.addWidget(self.OutputLink)

        self.setLayout(layout)

    def convert_URL(self):
        output_link = re.sub(r"https://drive\.google\.com/file/d/(.*?)/.*?\?usp=sharing",
       r"https://drive.google.com/uc?export=download&id=\1", self.EnterURL.text())
        # print(output_link)
        self.OutputLink.setText(output_link)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = GeneratorApp()
    demo.show()

    sys.exit(app.exec_())