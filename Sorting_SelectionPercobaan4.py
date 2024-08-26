# modifikasi dengan mengurutkan data list/array berdasarkan list/array level ke-dua index ke-0
print("---List/array level ke-dua index ke-0---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data Awal : ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if my_array[j][0] < my_array[index_of_minimum_elemen][0]:
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t
        
print("Data Setelah Diurutkan : ")
print(my_array)

# modifikasi dengan mengurutkan data list/array berdasarkan list/array level ke-dua index ke-1
print("---List/array level ke-dua index ke-1---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data Awal : ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if my_array[j][1] < my_array[index_of_minimum_elemen][1]:
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t
        
print("Data Setelah Diurutkan : ")
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

print("Data Awal : ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if sum(my_array[j]) < sum(my_array[index_of_minimum_elemen]):
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t
        
print("Data Setelah Diurutkan : ")
print(my_array)

# modifikasi dengan mengurutkan data list/array berdasarkan hasil perkalian elemen-elemen dari list/array di level ke-dua
print("---List/array level ke-dua hasil perkalian elemen-elemen---")
my_array = [
    [1,2],
    [3,9],
    [2,6],
    [9,8],
    [8,5]
    ]

print("Data Awal : ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if my_array[j][0] * my_array[j][1] < my_array[index_of_minimum_elemen][0] * my_array[index_of_minimum_elemen][1]:
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t

print("Data Setelah Diurutkan : ")
print(my_array)



