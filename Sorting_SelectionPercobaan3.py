# A - Z sorting
print("---A-Z sorting---")
my_array = ["B","A","D","C","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan: ",my_array)
for i,value_i in enumerate(my_array):
  index_of_minimum_elemen = i
  for j,value_j in enumerate(my_array):
    if i >= j:
      continue
    if my_array[j] < my_array[index_of_minimum_elemen]:
      index_of_minimum_elemen = j
  if i < index_of_minimum_elemen:
    t = my_array[i]
    my_array[i] = my_array[index_of_minimum_elemen]
    my_array[index_of_minimum_elemen] = t

print("Setelah diurutkan: ",my_array)

# Z - A sorting
print("---Z-A sorting---")
my_array = ["B","A","D","C","F","E","H","G","I","J","K","L","M","O","N","Q","P","R","T","S","U","V","X","W","Z","Y"]
print("Sebelum diurutkan: ",my_array)
for i,value_i in enumerate(my_array):
  index_of_minimum_elemen = i
  for j,value_j in enumerate(my_array):
    if i >= j:
      continue
    if my_array[j] > my_array[index_of_minimum_elemen]:
      index_of_minimum_elemen = j
  if i < index_of_minimum_elemen:
    t = my_array[i]
    my_array[i] = my_array[index_of_minimum_elemen]
    my_array[index_of_minimum_elemen] = t

print("Setelah diurutkan: ",my_array)

# String dari yang terpendek ke yang terpanjang 
print("---String terpendek ke terpanjang---")
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpendek ke terpanjang: ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if len(my_array[j]) < len(my_array[index_of_minimum_elemen]):
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t
        
print("Setelah diurutkan string terpendek ke terpanjang: ")
print(my_array)

# String dari yang terpanjang ke yang terpendek
print("---String terpanjang ke terpendek---") 
my_array = ["C","AA","B","DDD","F","EE","H","GG","I","JJJ","K","LLLL","M","OO","NN","Q","PP","R","T","SS","U","VV","X","W","Z","YY"]
print("Sebelum diurutkan string terpendek ke terpanjang: ")
print(my_array)

for i,value_i in enumerate(my_array):
    index_of_minimum_elemen = i
    for j,value_j in enumerate(my_array):
        if i >= j:
            continue
        if len(my_array[j]) > len(my_array[index_of_minimum_elemen]):
            index_of_minimum_elemen = j
    if i < index_of_minimum_elemen:
        t = my_array[i]
        my_array[i] = my_array[index_of_minimum_elemen]
        my_array[index_of_minimum_elemen] = t
        
print("Setelah diurutkan string terpendek ke terpanjang: ")
print(my_array)