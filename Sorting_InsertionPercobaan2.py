my_array = [7,5,1,10,3,6,2,4,8,9]
print(my_array)

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

print(my_array)
   