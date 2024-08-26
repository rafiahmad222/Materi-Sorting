my_array = [7,5,1,10,3,6,2,4,8,9]
print(my_array)
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

print(my_array)
