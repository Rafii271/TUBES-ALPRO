import mysql.connector
from prettytable import PrettyTable


class Data:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost", user="root", password="", database="dataparkir"
        )

        if self.db.is_connected():
            print("Succesfull Connect!")

    def insert_data(self, val):
        cursor = self.db.cursor()
        sql = "INSERT INTO datakendaraan(plat,jenis,tempat) VALUES(%s,%s,%s)"
        cursor.execute(sql, val)
        self.db.commit()
        print("{} Data telah Dimasukkan".format(cursor.rowcount))

    def showData(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM datakendaraan"
        cursor.execute(sql)
        result = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID", "JENIS", "PLAT", "TEMPAT"]

        for i in result:
            table.add_row(list(i))
        print(table)


class Main:
    def __init__(self):
        self.d1 = Data()
        self.cursor = self.d1.db.cursor()

    def dataParkir(self):
        plat = input("Masukan plat nomor kendaraan: ")
        jenis = input("Masukkan Jenis Kendaraan: ")
        tempat = input("Masukkan Tempat Parkir: ")
        val = (plat, jenis, tempat)
        self.d1.insert_data(val)

    def payment(self,total):
        print("Pilih Metode Pembayaran")
        print("1.Cash")
        print("2.Gopay")

        pay = int(input("Masukkan Pilihan: "))
        if pay == 1:
            print(f"pembayaran sukses dengan Cash senilai {total}, semoga selamat sampai tujuan")
        elif pay == 2:
            print(f"pembayaran sukses dengan Gopay senilai {total}, semoga selamat sampai tujuan")

    def harga(self):
        motor = 2000
        mobil = 5000
        truk = 8000
        sportcar = 10000
        indoor = 2000
        outdoor = 0

        plat = input("Masukkan Nomor Kendaraan: ")
        self.cursor.execute(
            "SELECT plat,jenis,tempat FROM datakendaraan WHERE plat=%s LIMIT 1", (plat,)
        )
        data = self.cursor.fetchone()
        if data is None:
            print("Data kendaraan tidak di temukan")

        elif plat in data:
            if data[1] == "Motor":
                jam = int(input("Masukkan Berapa lama Kendaraan Parkir: "))
                if data[2] == "Indoor":
                    total = jam * (motor + indoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total}"
                    )
                    self.payment(total)
                else:
                    total2 = jam * (motor + outdoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total2}"
                    )
                    self.payment(total)

            elif data[1] == "Mobil":
                jam = int(input("Masukkan Berapa lama kendaraan parkir: "))
                if data[2] == "Indoor":
                    total = jam * (mobil + indoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total}"
                    )
                    self.payment(total)
                else:
                    total2 = jam * (mobil + outdoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total2}"
                    )
                    self.payment(total)
            elif data[1] == "Truk":
                jam = int(input("Masukkan Berapa lama kendaraan parkir: "))
                if data[2] == "Indoor":
                    total = jam * (truk + indoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total}"
                    )
                    self.payment(total)
                else:
                    total2 = jam * (truk + outdoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total2}"
                    )
                    self.payment(total)
            elif data[1] == "Sportcar":
                jam = int(input("Masukkan Berapa lama kendaraan parkir: "))
                if data[2] == "Indoor":
                    total = jam * (sportcar + indoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total}"
                    )
                    self.payment(total)
                else:
                    total2 = jam * (sportcar + outdoor)
                    print(
                        f"Total Tahgihan Parkir {data[1]} Dengan Plat {data[0]} = {total2}"
                    )
                    self.payment(total)

    def tampilan(self):
        while True:
            print(
                """
            1. Daftar kendaraan
            2. Tagihan parkir
            3. Data kendaraan
            4. Keluar
            """
            )

            menu = int(input("Masukkan Menu: "))

            if menu == 1:
                self.dataParkir()
            elif menu == 2:
                self.harga()
            elif menu == 3:
                self.d1.showData()
            elif menu == 4:
                print("Berhasil Keluuar! ")
                break
            else:
                print("Salah Menu !")



if __name__ == "__main__":
    m1 = Main()
    m1.tampilan()
