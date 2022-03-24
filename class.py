import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class dataCivitas:
    list_nama = []
    list_studi = []

    def __init__(self,nama,programstudi):
        self.nama = nama
        dataCivitas.list_nama.append(self.nama)
        self.programstudi = programstudi
        dataCivitas.list_studi.append(self.programstudi)

    def tampilData(self):
        tabel_civitas = {"Nama Lengkap": dataCivitas.list_nama,
                         "Program Studi": dataCivitas.list_studi}

        a = pd.DataFrame(tabel_civitas)
        print(a.to_string(index=False))

class dataMahasiswa(dataCivitas):
    list_nim = []
    list_ipk = []
    list_ipkbagus = []
    list_ipkcukup = []
    list_ipkkurang = []
    list_ipkganiat = []

    def __init__(self,nama,programstudi,nim,ipk):
        super().__init__(nama,programstudi)
        self.__nim = nim
        dataMahasiswa.list_nim.append(self.__nim)
        self.ipk = ipk
        dataMahasiswa.list_ipk.append(self.ipk)
        if ipk > 3 and ipk <= 4:
            dataMahasiswa.list_ipkbagus.append(self.ipk)
        elif ipk > 2 and ipk <= 3:
            dataMahasiswa.list_ipkcukup.append(self.ipk)
        elif ipk > 1 and ipk <= 2:
            dataMahasiswa.list_ipkkurang.append(self.ipk)
        elif ipk >= 0 and ipk <= 1:
            dataMahasiswa.list_ipkganiat.append(self.ipk)
        else:
            pass

    def tampilData(self):
        tabel_mahasiswa = {"Nama": dataCivitas.list_nama,
                         "NIM": dataMahasiswa.list_nim,
                         "Program Studi": dataCivitas.list_studi,
                         "IPK": dataMahasiswa.list_ipk}

        a = pd.DataFrame(tabel_mahasiswa)
        print(a.to_string(index=False))

    def tampilIPK(self):
        x = ["0 - 1","1 - 2","2 - 3","3 - 4"]
        y = np.array([len(dataMahasiswa.list_ipkganiat),len(dataMahasiswa.list_ipkkurang),len(dataMahasiswa.list_ipkcukup),len(dataMahasiswa.list_ipkbagus)])
        plt.title("Sebaran Data IPK")
        plt.xlabel("Interval IPK")
        plt.ylabel("Jumlah Mahasiswa")
        plt.bar(x,y)
        plt.show()

pilihan = input("Ingin Input Data Civitas atau Mahasiswa atau Dosen ? : ")
if pilihan == "Civitas":
    while True:
        inputnama = input("Masukkan Nama : ")
        inputstudi = input("Masukkan Program Studi : ")
        civitas = dataCivitas(inputnama,inputstudi)
        ulang = input("Apakah ingin input lagi (y/t) ? :")
        if ulang == "t":
            break
    civitas.tampilData()
elif pilihan == "Mahasiswa":
    while True:
        inputnama = input("Masukkan Nama : ")
        inputstudi = input("Masukkan Program Studi : ")
        inputnim = input("Masukkan NIM : ")
        inputipk = float(input("Masukkan IPK : "))
        mahasiswa = dataMahasiswa(inputnama,inputstudi,inputnim,inputipk)
        ulang = input("Apakah ingin input lagi (y/t) ? :")
        if ulang == "t":
            break
    mahasiswa.tampilData()

    datasebaran = input("Apakah ingin menampilkan data sebaran IPK ? : ")
    if datasebaran == "y":
        mahasiswa.tampilIPK()
else:
    tampung = "Dosen"