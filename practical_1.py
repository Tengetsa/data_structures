# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

def heapsort(array):
    n = len(array)

    i = (n - 2) // 2
    while i >= 0:
        heapify(array, i, n)
        i = i - 1

    while n:
        array[n - 1] = del_element(array, n)
        n = n - 1


def heapify(array, i, size):
    left = LEFT(i)
    right = RIGHT(i)

    largest = i

    if left < size and array[left] > array[i]:
        largest = left

    if right < size and array[right] > array[largest]:
        largest = right

    if largest != i:
        replacement(array, i, largest)
        heapify(array, largest, size)


def del_element(array, size):
    if size <= 0:
        return -1

    top = array[0]

    array[0] = array[size - 1]

    heapify(array, 0, size - 1)

    return top

def replacement(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

array = [6, 4, 7, 1, 9, -2]

heapsort(array)

print(array)