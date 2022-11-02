import pandas as pd
import os as o
from os import system
list_nim=[]
list_nama = []
list_hadir=[]
list_tugas=[]
list_uts=[]
list_uas=[]
list_nilaiakhir=[]
ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan Nim anda : "))
    list_nama.append(input('Masukkan Nama anda : '))
    list_hadir.append(0.2*int(input('Masukkan Nilai Kehadiran : ')))
    list_tugas.append(0.25*int(input('Masukkan Nilai Tugas : ')))
    list_uts.append(0.25*int(input("Masukkan Nilai UTS anda :")))    
    list_uas.append(0.3*int(input("Masukkan Nilai UAS : ")))    
    list_nilaiakhir.append(list_hadir[i]+list_tugas[i]+list_uts[i]+list_uas[i])
    o.system('cls') 
mahasiswa = {
"NIM": list_nim,
"Nama Lengkap": list_nama,
"Nilai kehadiran": list_hadir,
"Nilai tugas": list_tugas,
"Nilai UTS": list_uts,
"Nilai UAS": list_uas,
"Nilai Akhir":list_nilaiakhir
}
data_mahasiswa = pd.DataFrame(mahasiswa)
print('================== Data Mahasiswa  =========================')
print(data_mahasiswa)
print('============================================================')