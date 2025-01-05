import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Input.ui', self)  
        
        # Koneksi ke database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="belajar3"
        )
        self.mycursor = self.mydb.cursor()

        # Load data ke tabel saat aplikasi dimulai
        self.load()

        # Menghubungkan tombol-tombol dengan fungsi CRUD
        self.pushButton.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.delete)

    def load(self):
        # Kosongkan tabel
        self.tableWidget.setRowCount(0)

        # Eksekusi query untuk mendapatkan data dari tabel
        self.mycursor.execute("SELECT * FROM user")
        data = self.mycursor.fetchall()

        # Isi tabel dengan data yang diperoleh
        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def save(self):
        # Ambil data dari input fields
        # id = self.lineEdit_5.text()
        nama = self.lineEdit_2.text()
        alamat = self.lineEdit_3.text()
        jenis_kelamin = self.lineEdit_4.text()
        jabatan = self.lineEdit_6.text()

        # Eksekusi perintah SQL untuk menambahkan data ke database
        sql = "INSERT INTO user (nama, alamat, jenis_kelamin, jabatan) VALUES (%s, %s, %s, %s)"
        val = (nama, alamat, jenis_kelamin, jabatan)
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
            id_to_edit = item.text()

            # Ambil data baru dari input line edit
            nama = self.lineEdit_2.text()
            alamat = self.lineEdit_3.text()
            jenis_kelamin = self.lineEdit_4.text()
            jabatan = self.lineEdit_6.text()

            # Eksekusi perintah SQL untuk mengedit data di database
            sql = "UPDATE user SET nama = %s, alamat = %s, jenis_kelamin = %s, jabatan = %s WHERE id = %s"
            val = (nama, alamat, jenis_kelamin, jabatan, id_to_edit)
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
            id_to_delete = item.text()

            # Eksekusi perintah SQL untuk menghapus data dari database
            sql = "DELETE FROM user WHERE id = %s"
            val = (id_to_delete,)
            self.mycursor.execute(sql, val)
            self.mydb.commit()

            # Hapus baris dari tabel setelah penghapusan data
            self.tableWidget.removeRow(baris)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
