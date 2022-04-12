import os.path
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import LabelBezier
import cv2
import math


class LabelBezierCurve(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = LabelBezier.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化

        self.init_ui()
        self.input_image = None
        self.input_image_backup = None
        self.Label_Start = False
        self.isMoving = False
        self.nearPointIndex = -1
        self.pControl = []
        self.saveFileName = None
        self.imgOriginalWidth = 0
        self.imgOriginalHeight = 0
        self.allFiles = []
        self.allFilesIndex = 0

        #self.ui.OpenFile.setEnabled(True)
        self.ui.OpenFile.clicked.connect(self.openfile)
        self.ui.LabelButton.clicked.connect(self.Label)
        self.ui.LabelDone.clicked.connect(self.LabelDone)
        self.ui.LabelReset.clicked.connect(self.LabelReset)
        self.ui.LabelSave.clicked.connect(self.LabelSave)
        self.ui.OpenFolder.clicked.connect(self.OpenFolder)
        self.ui.OpenNext.clicked.connect(self.LabelNext)
        self.ui.LabelPrevious.clicked.connect(self.LabelPrevious)

        self.ui.LabelDone.setEnabled(False)
        self.ui.LabelReset.setEnabled(False)

        #self.ui.ControlPointList.addItem('pt1:({0},{1})'.format(100,200))

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.show()

    class ControlPoint():
        def __init__(self):
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0

    def make_ControlPoint(self):
        return self.ControlPoint()

    # The first derivative of cubic Bezier curve at point t
    def BezierFirstDerivat(self,p0,p1,p2,p3,t):
        derivate = 3 * ((p1 - p0) * (1 - t) * (1 - t) + (p2 - p1) * t * (1 - t) + (p3 - p2) * t * t)
        return derivate

    # The second derivative of cubic Bezier curve at point t
    def BezierSecondDerivat(self,p0,p1,p2,p3,t):
        derivate = 6 * ((p2 - 2 * p1 + p0) * (1 - t) + (p3 - 2 * p2 + p1) * t)
        return derivate

    # Curvature of the Bezier curve use first derivative and second derivative
    def BezierCurvature(self,FirstDerivat_x,SecondDerivat_x,FirstDerivat_y,SecondDerivat_y):
        Curvature = math.fabs(FirstDerivat_x * SecondDerivat_y - SecondDerivat_x * FirstDerivat_y) / math.pow(
            math.sqrt(math.fabs(FirstDerivat_x * FirstDerivat_x + FirstDerivat_y * FirstDerivat_y)), 3)
        return Curvature

    def BSplineBase(self,x,t):
        if x == 0:
            return (-t*t*t + 3*t*t - 3*t + 1.0) / 6.0
        elif x == 1:
            return (3*t*t*t - 6*t*t + 4.0) / 6.0
        elif x == 2:
            return (-3*t*t*t + 3*t*t + 3*t + 1.0)/6.0
        elif x == 3:
            return t*t*t/6.0
        else:
            return 0

    def BSplinePoint(self,t,m,control_pt):
        point = self.make_ControlPoint()
        point.x = 0
        point.y = 0
        point.z = 0
        #i = m
        for k in range(4):
            n = m + k
            point.x = point.x + control_pt[n].x*self.BSplineBase(k, t)
            point.y = point.y + control_pt[n].y*self.BSplineBase(k, t)
        return point

    def DrawBezierCurve(self,control_pt,img):

        img_temp = img.copy()
        if len(control_pt)< 4 :
            return 0
        pt_pre = self.make_ControlPoint()
        pt_now = self.make_ControlPoint()
        pt_pre.x = 0
        pt_pre.y = 0
        pt_pre.z = 0

        for i in range(len(control_pt)):
            cv2.circle(img_temp, (control_pt[i].x, control_pt[i].y), 8, (255, 0, 0), 2)

        for j in range(0,len(control_pt)-3):
            for i in range(51):
                u = (float)(i)/50
                pt_now = self.BSplinePoint(u, j,control_pt)  # Bernstein(u, pt_temp)  BSplinePoint(u, j,control_pt)
                if i > 0:
                    cv2.line(img_temp,(int(pt_now.x),int(pt_now.y)),(int(pt_pre.x),int(pt_pre.y)),(0,255,0),2)
                pt_pre.x = pt_now.x
                pt_pre.y = pt_now.y

        return img_temp

    def openfile(self):
        openfile_name,imgType = QFileDialog.getOpenFileName(self, 'Select File', '', 'Image Files(*.bmp , *.jpg)')
        if openfile_name == None:
            return 0
        # In cv2.imread, to reading images in an absolute path, should replace '/' to '\\' in the path
        # Notice that there should not contain any chinese character in the path
        openfile_name = openfile_name.replace('/','\\')
        self.OpenAndShow(openfile_name)

    def OpenAndShow(self,file):

        openfile_name = file
        self.saveFileName = os.path.basename(openfile_name)
        self.saveFileName, extension = os.path.splitext(self.saveFileName)
        self.saveFileName = self.saveFileName + '.txt'

        self.input_image = cv2.imread(openfile_name)  # openfile_name  '0001.jpg'
        self.input_image_backup = cv2.imread(openfile_name)  # openfile_name

        self.imgOriginalHeight, self.imgOriginalWidth, _ = self.input_image.shape

        new_width = self.ui.ImageLabel.width()
        new_height = self.ui.ImageLabel.height()
        self.input_image = cv2.resize(self.input_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        self.input_image_backup = cv2.resize(self.input_image_backup, (new_width, new_height),
                                             interpolation=cv2.INTER_LINEAR)
        height, width, bytesPerComponent = self.input_image.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(self.input_image, cv2.COLOR_BGR2RGB, self.input_image)
        cv2.cvtColor(self.input_image_backup, cv2.COLOR_BGR2RGB, self.input_image_backup)

        QImg = QImage(self.input_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.ui.ImageLabel.setPixmap(pixmap)
        self.ui.ImageLabel.setCursor(Qt.CrossCursor)

        self.ui.OpenFile.setEnabled(True)
        #self.pControl.clear()


    def OpenFolder(self):
        Folder = QFileDialog.getExistingDirectory(self,'Choose Folder',os.getcwd())
        Folder = Folder.replace('/', '\\')
        self.allFiles = []
        self.allFilesIndex = 0
        if os.path.isdir(Folder):
            filelist = os.listdir(Folder)
            for f in filelist:
                f = Folder + '\\' + f
                self.allFiles.append(f)
            if len(self.allFiles) > 0:
                self.OpenAndShow(self.allFiles[self.allFilesIndex])

    def LabelNext(self):
        if self.allFilesIndex < len(self.allFiles)-1:
            self.allFilesIndex = self.allFilesIndex + 1
            self.OpenAndShow(self.allFiles[self.allFilesIndex])
        if self.allFilesIndex > 0:
            img_draw = self.DrawBezierCurve(self.pControl, self.input_image)
            self.showImage(img_draw)
    def LabelPrevious(self):
        if self.allFilesIndex > 0:
            self.allFilesIndex = self.allFilesIndex - 1
            self.OpenAndShow(self.allFiles[self.allFilesIndex])
        #if self.allFilesIndex > 0:
        img_draw = self.DrawBezierCurve(self.pControl, self.input_image)
        self.showImage(img_draw)

    def Label(self):
        self.Label_Start = True
        self.ui.LabelButton.setEnabled(False)
        self.ui.LabelDone.setEnabled(True)
        self.ui.LabelReset.setEnabled(True)

    def LabelDone(self):
        self.Label_Start = False
        self.ui.LabelButton.setEnabled(True)
        self.ui.LabelDone.setEnabled(False)
        self.ui.LabelReset.setEnabled(True)

    def LabelReset(self):
        self.pControl.clear()
        self.input_image_backup= self.input_image.copy()
        self.showImage(self.input_image)
        self.ui.LabelButton.setEnabled(True)
        self.ui.LabelDone.setEnabled(False)
        self.ui.LabelReset.setEnabled(False)

    def LabelSave(self):
        file = open('./data/{0}'.format(self.saveFileName),'w')
        for i in range(len(self.pControl)):
            height, width, bytesPerComponent = self.input_image.shape
            y = float(self.imgOriginalHeight)/height*self.pControl[i].y
            x = float(self.imgOriginalWidth)/width*self.pControl[i].x
            file.write('{0},{1}'.format(int(x),int(y)))
            file.write('\n')
        file.close()
        QMessageBox.information(self, "Info", "Data Saved!", QMessageBox.Yes, QMessageBox.Yes)

    def getNearPointIndex(self,mouse_pt):

        for i in range(len(self.pControl)):
            pt_x = self.pControl[i].x - mouse_pt.x  # + top
            pt_y = self.pControl[i].y - mouse_pt.y # + left
            dist = math.sqrt(pt_x*pt_x+pt_y*pt_y)
            if dist < 10:
                return i
        return -1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.Label_Start == True:
                top = self.ui.ImageLabel.x()
                left = self.ui.ImageLabel.y()

                pt1 = event.pos()
                x = pt1.x()
                y = pt1.y()
                pt = self.make_ControlPoint()
                pt.x = x - top
                pt.y = y - left

                self.nearPointIndex = self.getNearPointIndex(pt)
                if self.nearPointIndex != -1:
                    self.isMoving = True
                else:
                    self.isMoving = False
                    if len(self.pControl)==0 or len(self.pControl)==4:
                        self.pControl.append(pt)
                        self.pControl.append(pt)
                    elif len(self.pControl) > 4:
                        self.pControl.pop()
                        self.pControl.append(pt)
                        self.pControl.append(pt)
                    else:
                        self.pControl.append(pt)
                    if len(self.pControl) >=5:
                        img_draw = self.DrawBezierCurve(self.pControl,self.input_image)
                        self.showImage(img_draw)
                    else:
                        cv2.circle(self.input_image_backup, (pt.x, pt.y), 8, (255, 0, 0), 2)
                        self.showImage(self.input_image_backup)
                    self.updateList()


    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            pt1 = event.pos()
            if self.isMoving == True:
                top = self.ui.ImageLabel.x()
                left = self.ui.ImageLabel.y()
                self.pControl[self.nearPointIndex].x = pt1.x()-top
                self.pControl[self.nearPointIndex].y = pt1.y()-left
                self.updateList()
                img_draw = self.DrawBezierCurve(self.pControl, self.input_image)
                self.showImage(img_draw)

    def updateList(self):
        self.ui.ControlPointList.clear()
        for i in range(len(self.pControl)):
            self.ui.ControlPointList.addItem('pt{0} : ({1},{2})'.format(i, self.pControl[i].x, self.pControl[i].y))


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.isMoving == True:
                img_draw = self.DrawBezierCurve(self.pControl,self.input_image)
                self.showImage(img_draw)
                self.isMoving = False

    def showImage(self,img):
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.ui.ImageLabel.setPixmap(pixmap)


# 程序入口
if __name__ == '__main__':
    e = LabelBezierCurve()
    sys.exit(e.app.exec())