# modifikasi dengan mengurutkan data list/array berdasarkan list/array level ke-dua index ke-0
print("---List/array level ke-dua index ke-0---")
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
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element[0] >= my_array[j][0]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    
print("Data setelah diurutkan: ")
print(my_array)

# # modifikasi dengan mengurutkan data list/array berdasarkan list/array level ke-dua index ke-1
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
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element[1] >= my_array[j][1]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    
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
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element[0] + current_element[1] >= my_array[j][0] + my_array[j][1]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    
print("Data setelah diurutkan: ")
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

print("Data awal: ")
print(my_array)

for i,value_i in enumerate(my_array):
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element[0] * current_element[1] >= my_array[j][0] * my_array[j][1]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    
print("Data setelah diurutkan: ")
print(my_array)
    



