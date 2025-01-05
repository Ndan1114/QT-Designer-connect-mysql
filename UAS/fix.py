import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector

class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi('FormLogin.ui', self)
        self.setWindowTitle('Login From')
        self.pushButton.clicked.connect(self.login)
        self.show()
        self.kesempatan = 0

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if username == 'Admin' and password == 'admin123':
            self.close()
            self.a = menu()
            self.a.show()
            QMessageBox.information(self, 'Login Berhasil', 'Selamat Datang, Admin!')
        else:
            self.kesempatan += 1
            if self.kesempatan >= 3:
                QMessageBox.critical(self, 'Warning', 'anda salah dalam memasukan user sebanyak 3x.  EXIT.....')
                self.close()
            else:
                QMessageBox.warning(self, 'Gagal', 'username atau password salah')
                
class menu(QMainWindow):
    def __init__(self):
        super(menu, self).__init__()
        loadUi('menu2.ui', self)
        self.setWindowTitle('Menu')
        self.pushButton_2.clicked.connect(self.a)
        self.show()
        
    def a(self):
        self.hide()
        self.s = sempurna()
        self.s.show()
        
    # def b(self):
    #     self.hide()
    #     self.s = N()
    #     self.s.show()
    
class sempurna(QMainWindow):
    def __init__(self):
        super(sempurna, self).__init__()
        loadUi('Input2.ui', self)
        self.setWindowTitle('HRD')
        self.pushButton.clicked.connect(self.c)
        self.pushButton_2.clicked.connect(self.d)
        self.pushButton_14.clicked.connect(self.e)
        self.show()

    def c(self):
        self.stackedWidget.setCurrentIndex(0)
        self.show()

        # Koneksi ke database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="belajar3"
        )
        self.mycursor = self.mydb.cursor()

        # # Load data ke tabel saat aplikasi dimulai
        # self.tableWidget_2.setColumnWidth(0, 50)
        # self.tableWidget_2.setColumnWidth(1, 95)
        # self.tableWidget_2.setColumnWidth(2, 100)
        # self.tableWidget_2.setColumnWidth(3, 100)
        self.load()

        # Menghubungkan tombol-tombol dengan fungsi CRUD
        self.pushButton_7.clicked.connect(self.save)
        self.pushButton_8.clicked.connect(self.edit)
        self.pushButton_9.clicked.connect(self.delete)
        # self.pushButton_4.clicked.connect(self.pulang)    
    def load(self):
        # Menampilkan tabel 2
        # mbuh = [{"Status" : "Menikah", "Bonus" : "Rp.350.000", "Uang Makan" : "Rp.50.000"}, 
        #        {"Status" : "Lajang dan Cerai", "Bonus" : "Rp.150.000", "Uang Makan" : "Rp.50.000"}]
        # rows = 0
        # self.tableWidget_2.setRowCount(len(mbuh))
        # for mbuh in mbuh :
        #     self.tableWidget_2.setItem(rows, 0, QtWidgets.QTableWidgetItem(mbuh["Status"]))
        #     self.tableWidget_2.setItem(rows, 1, QtWidgets.QTableWidgetItem(mbuh["Bonus"]))
        #     self.tableWidget_2.setItem(rows, 2, QtWidgets.QTableWidgetItem(mbuh["Uang Makan"]))
        #     #self.tableWidget_2.setItem(rows, 3, QtWidgets.QTableWidgetItem(ora["Uang Makan"]))
        #     rows = rows+1
            
        # Kosongkan tabel
        self.tableWidget.setRowCount(0)

        # Eksekusi untuk mendapatkan data dari tabel
        self.mycursor.execute("SELECT * FROM user1")
        data = self.mycursor.fetchall()

        # Isi tabel dengan data yang diperoleh
        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def save(self):
        # Ambil data dari input fields
        # id = self.lineEdit_4.text()
        nama = self.lineEdit_3.text()
        alamat = self.lineEdit_2.text()
        jenis_kelamin = self.comboBox_2.currentText()
        jabatan = self.comboBox_3.currentText()
        status = self.comboBox_4.currentText()

        # Eksekusi perintah SQL untuk menambahkan data ke database
        sql = "INSERT INTO user1 (nama, alamat, jenis_kelamin, jabatan, status) VALUES (%s, %s, %s, %s, %s)"
        val = (nama, alamat, jenis_kelamin, jabatan, status)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

        # Muat ulang data setelah penambahan
        self.load()

    def edit(self):
        # Mendapatkan indeks baris yang dipilih
        selected_row = self.tableWidget.currentRow()

        if selected_row >= 0:
            # Mendapatkan nilai ID dari item baris yang dipilih
            item = self.tableWidget.item(selected_row, 0)
            edit = item.text()

            # Ambil data baru dari input line edit
            # id = self.lineEdit_4.text()
            nama = self.lineEdit_3.text()
            alamat = self.lineEdit_2.text()
            jenis_kelamin = self.comboBox_2.currentText()
            jabatan = self.comboBox_3.currentText()
            status = self.comboBox_4.currentText()

            # Eksekusi perintah SQL untuk mengedit data di database
            sql = "UPDATE user1 SET nama = %s, alamat = %s, jenis_kelamin = %s, jabatan = %s, status = %s WHERE id = %s"
            val = (nama, alamat, jenis_kelamin, jabatan, status, edit)
            self.mycursor.execute(sql, val)
            self.mydb.commit()

            # Muat ulang data setelah pengeditan
            self.load()

    def delete(self):
        # Mendapatkan indeks baris yang dipilih
        baris = self.tableWidget.currentRow()

        if baris >= 0:
            # Mendapatkan nilai ID dari item baris yang dipilih
            item = self.tableWidget.item(baris, 0)
            delete = item.text()

            # Eksekusi perintah SQL untuk menghapus data dari database
            sql = "DELETE FROM user1 WHERE id = %s"
            val = (delete,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()

            # Hapus baris dari tabel setelah penghapusan data
            self.tableWidget.removeRow(baris)
    def d(self):
        self.setWindowTitle('Progress Data')
        self.pushButton_6.clicked.connect(self.plot)
        # self.pushButton_2.clicked.connect(self.balik)
        self.stackedWidget.setCurrentIndex(1)
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
                plt.title('Progress Tahun 2024')
                # refresh canvas
                self.canvas.draw()        
    def e(self):
        self.stackedWidget.setCurrentIndex(2)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login()
    window.show()
    sys.exit(app.exec_())            
    