import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import mysql.connector

class c(QMainWindow):
    def __init__(self):
        super(c, self).__init__()
        loadUi('grafik.ui', self)
        self.setWindowTitle('Progress Data')
        self.pushButton.clicked.connect(self.plot)
        self.pushButton_2.clicked.connect(self.plot)
        self.show()
        
    # horizontal
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName('horizontalLayout')
        # canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # Selesai
        # Tambahan canvas
        self.horizontalLayout_2.addWidget(self.canvas)
        # selesai
        
    def plot(self):
        bulan = ['Jan', 'Feb', 'Mart', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des']
        # 2021 = combo box index 0
        # 2022 = combo box index 1
        # 2023 = combo box index 2
        # 2024 = combo box indes 3
        
        # untuk 2021
        if self.comboBox.currentIndex()==0:
                # hapus canvas
                self.figure.clear()
                nilai = np.array([200,200,80,90,67,45,78,180,35,78,87, 98])
                print(nilai)
                # buat bar
                plt.bar(bulan, nilai, color = 'red', width = 0.4)
                plt.xlabel('Bulan Dari Tahun')
                plt.title('Progress Tahun 2021')
                # refresh canvas
                self.canvas.draw()
        # untuk 2022
        if self.comboBox.currentIndex()==1:
                # hapus canvas
                self.figure.clear()
                nilai = np.array([80,150,60,20,27,45,60,200,90,78,87, 80])
                print(nilai)
                # buat bar
                plt.bar(bulan, nilai, color = 'red', width = 0.4)
                plt.xlabel('Bulan Dari Tahun')
                plt.title('Progress Tahun 2022')
                # refresh canvas
                self.canvas.draw()
        # untuk 2023
        if self.comboBox.currentIndex()==2:
                # hapus canvas
                self.figure.clear()
                nilai = np.array([100,180,90,85,87,82,90,40,35,95,87, 100])
                print(nilai)
                # buat bar
                plt.bar(bulan, nilai, color = 'red', width = 0.4)
                plt.xlabel('Bulan Dari Tahun')
                plt.title('Progress Tahun 2023')
                # refresh canvas
                self.canvas.draw()
        # untuk 2024
        if self.comboBox.currentIndex()==3:
                # hapus canvas
                self.figure.clear()
                nilai = np.array([200,200,90,80,150,95,80,150,80,78,87, 200])
                print(nilai)
                # buat bar
                plt.bar(bulan, nilai, color = 'red', width = 0.4)
                plt.xlabel('Bulan Dari Tahun')
                plt.title('Progress Tahun 2024')
                # refresh canvas
                self.canvas.draw()        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = c()
    window.show()
    sys.exit(app.exec_())
    
                