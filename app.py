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

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # transforma a imagem colorida em uma imagem em grayscale
        noise = np.random.uniform (size=gray_frame.shape)
        gray_frame[noise>.9] = 255 # noise salt
        gray_frame[noise<.1] = 0 # noise pepper

        #filtered_image = np.zeros_like(gray_frame).astype('uint8') # criando imagem onde será armazenada a imagem filtrada
        filtered_image = mediana.mediana(gray_frame.astype('int'))

        self.originalImage.setPixmap (self.convert_cv_qt(gray_frame.astype('uint8'))) # atribuicao do novo valor do pixmap do label
        self.filteredImage.setPixmap (self.convert_cv_qt(filtered_image))

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

# def main ():
#     cam = camera().astype('int')
#     noise = np.random.uniform (size=cam.shape)
#     cam[noise>.9] = 255 # noise salt
#     cam[noise<.1] = 0 # noise pepper
#     # cam = cam/np.max(cam)
#     n=cam.shape[0]
#     # filtragem para remocao de ruidos
#     cam_blur = mediana.mediana(cam)
#     # impressao dos resultados
#     _,ax = plt.subplots(1,2)
#     ax[0].imshow(cam,cmap='gray')
#     ax[1].imshow(cam_blur,cmap='gray')
#     ax[0].set_title('Imagem Original')
#     ax[1].set_title('Imagem Borrada')
#     plt.savefig ('resultado.png')

# if __name__=='__main__':
#     main()