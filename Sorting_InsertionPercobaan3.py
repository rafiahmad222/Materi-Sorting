# A-Z sorting
print("---A-Z sorting---")
my_array = ["C","A","B","D","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan A-Z: ",my_array)

for i,value_i in enumerate(my_array):
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element >= my_array[j]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element

print("Setelah diurutkan A-Z: ",my_array)
# Z - A sorting
print("---Z-A sorting---")
my_array = ["C","A","B","D","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan Z-A: ",my_array)

for i,value_i in enumerate(my_array):
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if current_element <= my_array[j]:
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element

print("Setelah diurutkan Z-A: ",my_array)

# mengurutkan data list/array yang berisi sekumpulan string berdasarkan panjang string dari yang terpendek ke yang terpanjang
print("---String terpendek ke terpanjang---")
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpendek ke terpanjang: ")
print(my_array)

for i,value_i in enumerate(my_array):
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if len(current_element) >= len(my_array[j]):
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    

print("Setelah diurutkan string terpendek ke terpanjang: ")
print(my_array)

# mengurutkan data list/array yang berisi sekumpulan string berdasarkan panjang string dari yang terpanjang ke yang terpendek
print("---String terpanjang ke terpendek---")
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpanjang ke terpendek: ")
print(my_array)

for i,value_i in enumerate(my_array):
    if i == 0:
      continue

    current_element = my_array[i]
    j = i-1
    while j >= 0:
      if len(current_element) <= len(my_array[j]):
        break
      my_array[j+1] = my_array[j]
      j = j-1

    my_array[j+1] = current_element
    

print("Setelah diurutkan string terpanjang ke terpendek: ")
print(my_array)