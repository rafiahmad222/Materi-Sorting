# mengurutkan data list/array berdasarkan list/array level ke-dua index ke-0
print("---List/array level ke-dua index ke-0---")
my_array = [ # list/array yang akan diurutkan
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data awal: ") # menampilkan data awal
print(my_array) # menampilkan data awal
for i,value_i in enumerate(my_array): # perulangan pertama untuk mengecek bilangan pertama
    for j,value_j in enumerate(my_array): # perulangan kedua untuk mengecek bilangan kedua
        if i <= j: # jika bilangan pertama lebih kecil dari bilangan kedua maka akan di lanjutkan
            continue
        if my_array[i][0] < my_array[j][0]: # jika bilangan pertama lebih besar dari bilangan kedua maka menjalankan perintah dibawah
            t = my_array[i] # menyimpan bilangan pertama ke dalam variabel t
            my_array[i] = my_array[j] # mengganti bilangan pertama dengan bilangan kedua
            my_array[j] = t # mengganti bilangan kedua dengan bilangan pertama
            
print("Data setelah diurutkan: ")
print(my_array)

# mengurutkan data list/array berdasarkan list/array level ke-dua index ke-1
print("---List/array level ke-dua index ke-1---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data awal: ")
print(my_array)

for i,value_i in enumerate(my_array):
    for j,value_j in enumerate(my_array):
        if i <= j:
            continue
        if my_array[i][1] < my_array[j][1]:
            t = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = t

print("Data setelah diurutkan: ")   
print(my_array)

# modifikasi dengan mengurutkan data list/array berdasarkan hasil penjumlah elemen-elemen dari list/array di level ke-dua
print("---List/array level ke-dua hasil penjumlah elemen-elemen---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data awal: ")
print(my_array)

for i,value_i in enumerate(my_array):
    for j,value_j in enumerate(my_array):
        if i <= j:
            continue
        if my_array[i][0] + my_array[i][1] < my_array[j][0] + my_array[j][1]:
            t = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = t
            
print("Data setelah diurutkan: ")
print(my_array)


# modifikasi dengan mengurutkan data list/array berdasarkan hasil perkalian elemen-elemen dari list/array di level ke-dua dan memunculkan hasil perkalian elemen-elemen
print("---List/array level ke-dua hasil perkalian elemen-elemen---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data awal: ")
print(my_array)

for i,value_i in enumerate(my_array):
    for j,value_j in enumerate(my_array):
        if i <= j:
            continue
        if my_array[i][0] * my_array[i][1] < my_array[j][0] * my_array[j][1]:
            t = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = t
            
print("Data setelah diurutkan: ")
print(my_array)


 
            
