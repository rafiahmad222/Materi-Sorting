# Buatlah program Python yang mengurutkan abjad A - Z dan Z - A sesuai kaidah urutan abjad menggunakan algoritma Insertion Sort. dengan input variable abjad = 'BCAPZUKSJODWHXGTRFVEQILNMY'.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

abjad = 'BCAPZUKSJODWHXGTRFVEQILNMY'
print(insertion_sort(list(abjad)))




