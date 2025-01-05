import mysql.connector
# import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "belajar3"
)

def masukan(db):
    id = input("Masukan id Karyawan :")
    nama = input("Masukan Nama : ")
    alamat = input("Masukan Alamat :")
    value = (id, nama, alamat)
    cursor = db.cursor()
    sql = "INSERT INTO user (id, nama, alamat) VALUES (%s, %s, %s)"
    cursor.execute(sql, value)
    db.commit
    print("{} data berhasil disimpan".format(cursor.rowcount))
    
def tampilkan(db):
    cursor = db.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    if cursor.rowcount < 0:
        print("Tidak ad data")
    else:
        for data in results:
            print(data)
            
def update(db):
    cursor = db.cursor()
    tampilkan(db)
    id = input("pilih id karyawan >")
    nama = input("Nama Baru :")
    alamat = input("alamat baru :")
    
    sql = "UPDATE user SET nama = %s, alamat = %s WHERE id = %s"
    value = (nama, alamat, id)
    cursor.execute(sql, value)
    db.commit()
    print("{} data berhasil diuah".format(cursor.rowcount))
    
def hapus(db):
    cursor = db.cursor()
    tampilkan(db)
    id = input("pilih id karyawan >")
    sql = "DELETE FROM user WHERE id = %s"
    value = (id)
    cursor.execute(sql, value)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    
def menu(db):
    print("======== APLIKASI DATABASE PYTHON ========")
    print("1. Masukan Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("==========================================")
    daftar = input("Pilih Menu >")
    
    # os.system("clear")

    if daftar == "1":
        masukan(db)
    elif daftar == "2":
        tampilkan(db)
    elif daftar == "3":
        update(db)
    elif daftar == "4":
        hapus(db)
    elif daftar == "0":
        exit()
    else:
        print("Menu Salah!")
        
if __name__ == "__main__":
    while(True):
        menu(db)
    