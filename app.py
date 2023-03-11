from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from AP04 import Ui_MainWindow
import numpy as np
import mediana
from skimage.data import camera
from skimage.io import imsave
import matplotlib.pyplot as plt
import sys
import cv2 

class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow,self).__init__ (*args, **kwargs)
        self.setupUi (self)
        self.setWindowTitle ("Filtro da Mediana")
        self.cap = cv2.VideoCapture(0) # objeto que representa a webcam    
        self.timer = QTimer() # objeto que representa um cronometro
        self.timer.timeout.connect (self.processar_frame) # ligacao dos disparos do cronometro a uma funcao em Python
        self.timer.start (50) # start do cronometro com disparos regulares a cada 50 ms
       

    def convert_cv_qt(self, cv_img): # funcao usada para converter opencv para qt
        h, w = cv_img.shape
        bytes_per_line = w
        convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap.fromImage(convert_to_Qt_format)

    def processar_frame(self):
        ret, frame = self.cap.read() # leitura de um frame do video

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype('uint8') # transforma a imagem colorida em uma imagem em grayscale
        noise = np.random.uniform (size=gray_frame.shape)

        # aplicando o ruído sal e pimenta na imagem capturada pela webcam, para podermos comparar o resultado da mediana

        gray_frame[noise>.9] = 255 # noise salt 
        gray_frame[noise<.1] = 0 # noise pepper

        filtered_image = mediana.mediana(gray_frame) # gerando a imagem filtrada a partir da imagem original usando a função da mediana

        self.originalImage.setPixmap (self.convert_cv_qt(gray_frame)) # atrinuindo a imagem original com ruidos na label da esquerda
        self.filteredImage.setPixmap (self.convert_cv_qt(filtered_image)) # atrubuindo a imagem filtrada pela mediana na label da direita

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()