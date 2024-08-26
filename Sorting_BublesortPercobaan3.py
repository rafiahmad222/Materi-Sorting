# A-Z sorting
print("---A-Z sorting---") # menampilkan tulisan A-Z sorting
my_array = ["A","C","B","D","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan: ",my_array) # menampilkan tulisan Sebelum diurutkan
for i,value_i in enumerate(my_array): # perulangan pertama untuk mengecek huruf pertama
  for j,value_j in enumerate(my_array): # perulangan kedua untuk mengecek huruf kedua
    if i >= j: # jika huruf pertama lebih besar dari huruf kedua maka akan di lanjutkan
      continue # melanjutkan perintah
    if my_array[i] > my_array[j]: # jika huruf pertama lebih besar dari huruf kedua maka menjalankan perintah dibawah
      t = my_array[i] # menyimpan huruf pertama ke dalam variabel t
      my_array[i] = my_array[j] # mengganti huruf pertama dengan huruf kedua
      my_array[j] = t # mengganti huruf kedua dengan huruf pertama

print("Setelah diurutkan: ",my_array)

# Z - A sorting
print("---Z-A sorting---")
my_array = ["A","C","B","D","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan: ",my_array)
for i,value_i in enumerate(my_array):
  for j,value_j in enumerate(my_array):
    if i <= j:
      continue
    if my_array[i] > my_array[j]:
      t = my_array[i]
      my_array[i] = my_array[j]
      my_array[j] = t

print("Setelah diurutkan: ",my_array)

# String dari yang terpendek ke yang terpanjang menggunakan bubble sort
print("---String terpendek ke terpanjang---")
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpendek ke terpanjang: ")
print(my_array)

for i,value_i in enumerate(my_array):
  for j,value_j in enumerate(my_array):
    if i >= j:
      continue
    if len(my_array[i]) > len(my_array[j]):
      t = my_array[i]
      my_array[i] = my_array[j]
      my_array[j] = t
      
print("Setelah diurutkan string terpendek ke terpanjang: ")
print(my_array)

# String dari yang terpanjang ke yang terpendek menggunakan bubble sort
print("---String terpanjang ke terpendek---")
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpanjang ke terpendek: ")
print(my_array)

for i,value_i in enumerate(my_array):
    for j,value_j in enumerate(my_array):
        if i <= j:
            continue
        if len(my_array[i]) > len(my_array[j]):
            t = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = t
        
print("Setelah diurutkan string terpanjang ke terpendek: ")
print(my_array)