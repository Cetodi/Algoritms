def merge_sort(arr):  # сортировка слиянием
    if len(arr) > 1:
        mid = len(arr) // 2  # находим середину массива
        left_half = arr[:mid]
        right_half = arr[mid:]  # делим массив на две части

        merge_sort(left_half)  # рекурсивно сортируем левую часть
        merge_sort(right_half)  # рекурсивно сортируем правую часть

        merge(arr, left_half, right_half)  # сливаем остортированные части


def merge(arr, left, right):
    i = j = k = 0  # индексы для перебора left, right и основного массива arr
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


array = [12, 1, 12, 7, 8, 1, 23, 3, 5, 9, 5, 8, 8]
merge_sort(array)
print("Отсортированный массив:", array)


def binary_search(list, item):
    low, high = 0, len(list) - 1  # границы списка
    while low <= high:
        mid = (low + high) // 2  # средний элемент
        guess = list[mid]
        if guess == item:  # значение найдено
            return mid
        if guess > item:  # много
            high = mid - 1
        else:  # мало
            low = mid + 1
    return None  # значение не найдено


print(binary_search(array, 7))
print(binary_search(array, -1))


def left_board(A, key):
    left, right = -1, len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left


def right_board(A, key):
    left, right = -1, len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swaped = False  #  flag для остжеивания совершения обменов
        for j in range(n - i - 1):  #  элементы сами всплывают и после каждого цикла элементов что стоят уже на месте всё больше и больше
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:  #  если не менялись, значит список остортирован
            break
    return arr

buarr = [64, 32, 25, 12, 22, 11, 90]
print("Исходный массив:", buarr)
print("Отсортированный массив:", bubble_sort(buarr))