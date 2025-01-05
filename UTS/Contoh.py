import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import mysql.connector

class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi('FormLogin.ui', self)
        self.setWindowTitle('Login From')
        self.pushButton.clicked.connect(self.login)
        self.show()

    def login(self):
           username = self.lineEdit.text()
           password = self.lineEdit_2.text()
           if self.cek(username, password):
               print("Login")
               self.hide()
           else:
               print("Gagal")
    def cek(self, username, password):
        try:
            db = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "belajar3"
            )
            cursor = db.cursor()
            sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            cursor.close()
            db.close()
            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Eror :", err)
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login()
    window.show()
    sys.exit(app.exec_())
    