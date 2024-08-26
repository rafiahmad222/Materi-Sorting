
#Output 1
def bubble_sort(list_angka):
    for i in range(len(list_angka)):
        for j in range(len(list_angka)-1):
            if list_angka[j][0] > list_angka[j+1][0]:
                list_angka[j], list_angka[j+1] = list_angka[j+1], list_angka[j]
    return list_angka

list_angka = [[5, 2], [4, 6], [1, 3], [8,7]]

print(bubble_sort(list_angka))

#Output 2
def bubble_sort(list_angka):
    for i in range(len(list_angka)):
        for j in range(len(list_angka)-1):
            if list_angka[j][1] > list_angka[j+1][1]:
                list_angka[j], list_angka[j+1] = list_angka[j+1], list_angka[j]
    return list_angka

list_angka = [[5, 2], [4, 6], [1, 3], [8,7]]

print(bubble_sort(list_angka))

#Output 3
def bubble_sort(list_angka):
    for i in range(len(list_angka)):
        for j in range(len(list_angka)-1):
            if list_angka[j][0] > list_angka[j+1][1]:
                list_angka[j], list_angka[j+1] = list_angka[j+1], list_angka[j]
    return list_angka

list_angka = [[5, 2], [4, 6], [1, 3], [8,7]]

print(bubble_sort(list_angka))