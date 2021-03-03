import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import win32con, win32gui, win32api, win32security




def hide_console():

    hide_me = win32gui.GetForegroundWindow()

    win32gui.ShowWindow(hide_me, win32con.SW_HIDE)


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://172.20.10.3:8081/admin'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

def main():
    hide_console()
    app = QApplication(sys.argv)
    QApplication.setApplicationName('PharmeliTech')
    window = MainWindow()
    app.exec_()

main()