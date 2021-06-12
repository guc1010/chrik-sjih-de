# 主程序入口

import sys
from PyQt5.QtWidgets import *
import Ui_kraihmjenh

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_kraihmjenh.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())