my_array = [7,5,1,10,3,6,2,4,8,9] # bilangan yang akan diurutkan
print(my_array) # menampilkan bilangan sebelum diurutkan
for i,value_i in enumerate(my_array): # perulangan pertama untuk mengecek bilangan pertama 
  for j,value_j in enumerate(my_array): # perulangan kedua untuk mengecek bilangan kedua
    if i >= j: # jika bilangan pertama lebih besar dari bilangan kedua maka akan di lanjutkan
      continue
    if my_array[i] > my_array[j]: # jika bilangan pertama lebih besar dari bilangan kedua maka menjalankan perintah dibawah
      t = my_array[i] # menyimpan bilangan pertama ke dalam variabel t
      my_array[i] = my_array[j] # mengganti bilangan pertama dengan bilangan kedua
      my_array[j] = t # mengganti bilangan kedua dengan bilangan pertama

print(my_array) # menampilkan bilangan setelah diurutkan
