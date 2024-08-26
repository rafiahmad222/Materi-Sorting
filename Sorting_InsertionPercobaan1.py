my_array = [7,5,1,10,3,6,2,4,8,9] # bilangan yang akan diurutkan
print(my_array) # menampilkan bilangan sebelum diurutkan

for i,value_i in enumerate(my_array): # perulangan pertama untuk mengecek bilangan pertama
    if i == 0: # jika bilangan pertama sama dengan 0 maka akan di lanjutkan
      continue # melanjutkan perintah

    current_element = my_array[i] # menyimpan bilangan pertama ke dalam variabel current_element
    j = i-1 # menyimpan bilangan pertama ke dalam variabel j dikurangi 1
    while j >= 0: # jika bilangan pertama lebih besar dari 0 maka akan di lanjutkan
      if current_element >= my_array[j]: # jika current_element lebih besar sama dengan bilangan pertama maka akan di break
        break
      my_array[j+1] = my_array[j] # mengganti bilangan pertama dengan bilangan kedua
      j = j-1 # mengurangi bilangan pertama dengan 1

    my_array[j+1] = current_element # mengganti bilangan pertama dengan current_element

print(my_array) # menampilkan bilangan setelah diurutkan
   