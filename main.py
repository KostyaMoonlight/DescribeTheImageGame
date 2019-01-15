import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from image_processing import ImageProcessor
import design
import game_design
import cv2
import re

class Menu(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OpenImageButton.clicked.connect(self.open_image)
        self.StartGameButton.clicked.connect(self.start_game)
        self.processor = None
        
        
    def open_image(self):

        self.file = QtWidgets.QFileDialog.getOpenFileName(self, "Select image")
        
            

    def start_game(self):
        w, h = self.__get_wh()
        if self.file:
            if h > 1 and w > 1:
                self.processor = ImageProcessor(self.file[0], (w, h), self.__get_new_size())
                self.matrix = self.processor.get_image_matrix()
        if self.processor:
            self.game = Game(self.processor.size, self.matrix)
            self.game.show()

    def __get_wh(self):
        return self.spinBox_w.value(), self.spinBox_h.value()

    def __get_new_size(self):  
        if self.newSize.text() and re.fullmatch("[0-9]+x[0-9]+", self.newSize.text()):
            return [int(value) for value in self.newSize.text().split("x")]
        return None;
 
class Game(QtWidgets.QMainWindow, game_design.Ui_GameWindow):
    def __init__(self, size, matrix):
        super().__init__()
        self.setupUi(self)
        self.resize(size[1],size[0])
        self.matrix=matrix
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                
                w ,h = elem.shape[0],elem.shape[1]
                btn = QtWidgets.QToolButton(self)
                
                btn.resize(h, w)
                self.set_img(btn, i,j,'black.jpg')
                btn.move(j*h,i*w)
                btn.clicked.connect(self.set_img(btn, i, j))
             
                
    def set_img(self, btn, i, j, name = 'tmp.jpg'):
        def _set_img():
            img = self.matrix[i][j]
            cv2.imwrite('tmp.jpg', img)
            w ,h = img.shape[0],img.shape[1]
            btn.setIcon(QtGui.QIcon(name))
            iconSize = QtCore.QSize(h, w)
            btn.setIconSize(iconSize)
        return _set_img

        
           


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()