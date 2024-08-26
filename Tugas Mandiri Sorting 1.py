# buat program untuk  membaca isi kamus csv. Program tersebut bisa menampilkan isi kamus secara terurut 1) berdasar kata bahasa Inggris 2) atau kata terjemahnya. program tersebut memberi pilihan user untuk melakukan sorting menggunakan beberapa algoritma. Beberapa alternatif algoritma sorting yang disediakan oleh kamus : 1) bubble sort 2) selection sort 3) Insertion sort
import csv
import os

iterasi = [0]
kamus_indo = []
kamus_ing = []
kamus = []
urut = []
fix = []

with open('kamus.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            kamus.append(row)
        
for i in range(len(kamus)):
        kamus_indo.append(kamus[i][0])
        kamus_ing.append(kamus[i][1])

def gabungan():
    os.system('cls')
    
    print('-'*50)
    print('Menu :')
    print('1. Sorting berdasarkan kata bahasa Indonesia')
    print('2. Sorting berdasarkan kata bahasa Inggris')
    print('3. Keluar')
    print('-'*50)
    pilihan = int(input('Masukkan pilihan : '))
    
    if pilihan == 1:
        for i in range(len(kamus_indo)):
            urut.append([kamus_indo[i], kamus_ing[i]])
            
    elif pilihan == 2:
        for i in range(len(kamus_ing)):
            urut.append([kamus_ing[i], kamus_indo[i]])
            
    else:
        print('Terima kasih')       
        exit()
        
        
def bubble_sort(urut):
    n = len(urut)
    for i in range(n):
        iterasi[0] += 1
        for j in range(0, n-i-1):
            if urut[j] > urut[j+1]:
                urut[j], urut[j+1] = urut[j+1], urut[j]
                iterasi[0] += 1
    return urut

def selection_sort(urut):
    n = len(urut)
    for i in range(n):
        iterasi[0] += 1
        min_idx = i
        for j in range(i+1, n):
            if urut[min_idx] > urut[j]:
                min_idx = j
                iterasi[0] += 1
        urut[i], urut[min_idx] = urut[min_idx], urut[i]
    return urut

def insertion_sort(urut):
    for i in range(1, len(urut)):
        iterasi[0] += 1
        key = urut[i]
        j = i-1
        while j >= 0 and key < urut[j]:
            urut[j + 1] = urut[j]
            j -= 1
            iterasi[0] += 1
        urut[j + 1] = key
    return urut

def tampil():
    os.system('cls')
    print('-'*50)
    print('Menu :')
    print('1. Bubble Sort')
    print('2. Selection Sort')
    print('3. Insertion Sort')
    print('4. Keluar')
    print('-'*50)
    pilihan = int(input('Masukkan pilihan : '))
    
    if pilihan == 1:
        bubble_sort(urut)
        for i in range(len(urut)):
            print(f'{urut[i][0]} : {urut[i][1]}')
        print(f'Jumlah iterasi : {iterasi[0]}')
    elif pilihan == 2:
        selection_sort(urut)
        for i in range(len(urut)):
            print(f'{urut[i][0]} : {urut[i][1]}')
        print(f'Jumlah iterasi : {iterasi[0]}')
    elif pilihan == 3:
        insertion_sort(urut)
        for i in range(len(urut)):
            print(f'{urut[i][0]} : {urut[i][1]}')
        print(f'Jumlah iterasi : {iterasi[0]}')
    else:
        print('Terima kasih')
        exit()
        
gabungan()
tampil()

    

                        
