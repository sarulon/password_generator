from password_generator import Ui_MainWindow as ui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import string
import random
import sys

class Password(ui, QMainWindow):
    p = f"{string.ascii_letters}{string.digits}"
    temp = ""
    def __init__(self, parent=None):
        self.threadpool = QThreadPool()
        super(Password, self).__init__(parent)
        self.setupUi(self)
        self.start.clicked.connect(self.generate)

    def generate(self):
        pw = ""
        if int(self.spec_chars.checkState()) == 0:
            pw = self.p
        elif int(self.spec_chars.checkState()) == 2:
            pw = f"{self.p}{string.punctuation}"
        self.temp = random.sample(pw, self.password_length.value())
        password = "".join(self.temp)
        print(pw)
        self.lineEdit.setText(password)
    

def main():
    try:
       app = QApplication(sys.argv)
       ex = Password()
       ex.show()
       sys.exit(app.exec_())
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()