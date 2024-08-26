# Terdapat sebuah daftar nama mahasiswa berbentuk CSVi. Dengan kolom  kelas, NIM, nama, nilai. Buatlah sebuah program  yang membaca dan  menampilkan daftar tersebut berdasar nilai. untuk mahasiswa yang memiliki nilai sama, maka akan di sorting berdasarkan nama. Gunakan selection sort untuk mensorting nilai dan Insertion sort untuk mensorting nama bagi mahasiswa yang nilainya sama
import csv

def nilai(mahasiswa):
    for i in range(len(mahasiswa)):
        max = i
        for j in range(i+1, len(mahasiswa)):
            if mahasiswa[j][3] > mahasiswa[max][3]:
                max = j
            elif mahasiswa[j][3] == mahasiswa[max][3] and mahasiswa[j][2] < mahasiswa[max][2]:
                    max = j
        mahasiswa[i], mahasiswa[max] = mahasiswa[max], mahasiswa[i]
    return mahasiswa
        
        
def nama(mahasiswa):
    for i in range(1, len(mahasiswa)):
        key = mahasiswa[i]
        j = i-1
        while j >=0 and key[2] < mahasiswa[j][2]:
            mahasiswa[j+1] = mahasiswa[j]
            j -= 1
        mahasiswa[j+1] = key
    return mahasiswa

def nilai_nama():
    with open('mahasiswa.csv', 'r') as file:
        baca_csv = csv.reader(file, delimiter=',')
        mahasiswa = [row for row in baca_csv]
        
    nilai_urut = nilai(mahasiswa)
    nilai_akhir = None
    nama_urut = []
    
    for x in range(len(nilai_urut)):
        if nilai_akhir != nilai_urut[x][3]:
            if nama_urut:
                nama_urut = nama(nama_urut)
                for j in nama_urut:
                    print(" ".join(j))
                nama_urut = []
            nama_urut.append(nilai_urut[x])
            nilai_akhir = nilai_urut[x][3]
        else:
            nama_urut.append(nilai_urut[x])
            nilai_akhir = nilai_urut[x][3]
    if nama_urut:
        nama_urut = nama(nama_urut)
        for j in nama_urut:
            print(" ".join(j))
            
nilai_nama()
  

    