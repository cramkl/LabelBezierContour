import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import LabelBezier
import cv2


class LabelBezierCurve(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = LabelBezier.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()
        self.input_image = None
        self.Label_Start = False

        self.ui.OpenFile.clicked.connect(self.openfile)
        self.ui.LabelButton.clicked.connect(self.Label)

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.show()

    def openfile(self):
        openfile_name,imgType = QFileDialog.getOpenFileName(self, 'Select File', '', 'Image Files(*.bmp , *.jpg)')
        #jpg = QPixmap(openfile_name).scaled(self.ui.ImageLabel.width(), self.ui.ImageLabel.height())
        #self.ui.ImageLabel.setPixmap(jpg)

        # In cv2.imread, to reading images in an absolute path, should replace '/' to '\\' in the path
        # Notice that there should not contain any chinese character in the path
        openfile_name = openfile_name.replace('/','\\')
        self.input_image = cv2.imread('internet.jpg')  #openfile_name

        new_width = self.ui.ImageLabel.width()
        new_height = self.ui.ImageLabel.height()
        self.input_image = cv2.resize(self.input_image,(new_width, new_height),interpolation=cv2.INTER_LINEAR)
        height, width, bytesPerComponent = self.input_image.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(self.input_image, cv2.COLOR_BGR2RGB, self.input_image)
        #cv2.circle(self.input_image, (100, 100), 5, (255, 0, 0), 1)
        QImg = QImage(self.input_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.ImageLabel.setCursor(Qt.CrossCursor)

    def Label(self):
        self.Label_Start = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.Label_Start == True:
                pt = event.globalPos()
                pt1 = event.pos()
                x = pt1.x()
                y = pt1.y()
                top = self.ui.ImageLabel.x()
                left = self.ui.ImageLabel.y()
                x = x - top
                y = y - left
                cv2.circle(self.input_image,(x,y),5,(255,0,0),1)
                self.showImage()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            test_move = 1

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            test_up = 1

    def showImage(self):
        height, width, bytesPerComponent = self.input_image.shape
        bytesPerLine = 3 * width
        QImg = QImage(self.input_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.ui.ImageLabel.setPixmap(pixmap)



# 程序入口
if __name__ == '__main__':
    e = LabelBezierCurve()
    sys.exit(e.app.exec())