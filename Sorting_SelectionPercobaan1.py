my_array = [7,5,1,10,3,6,2,4,8,9] # bilangan yang akan diurutkan
print(my_array) # menampilkan bilangan sebelum diurutkan
for i,value_i in enumerate(my_array): # perulangan pertama untuk mengecek bilangan pertama
  index_of_minimum_elemen = i # menyimpan bilangan pertama ke dalam variabel index_of_minimum_elemen
  for j,value_j in enumerate(my_array): # perulangan kedua untuk mengecek bilangan kedua
    if i >= j: # jika bilangan pertama lebih besar dari bilangan kedua maka akan di lanjutkan
      continue 
    if my_array[j] < my_array[index_of_minimum_elemen]: # jika bilangan kedua lebih kecil dari bilangan pertama maka menjalankan perintah dibawah
      index_of_minimum_elemen = j # menyimpan bilangan kedua ke dalam variabel index_of_minimum_elemen
  if i < index_of_minimum_elemen: # jika bilangan pertama lebih kecil dari bilangan kedua maka akan di lanjutkan
    t = my_array[i] # menyimpan bilangan pertama ke dalam variabel t
    my_array[i] = my_array[index_of_minimum_elemen] # mengganti bilangan pertama dengan bilangan kedua
    my_array[index_of_minimum_elemen] = t # mengganti bilangan kedua dengan bilangan pertama 

print(my_array)
