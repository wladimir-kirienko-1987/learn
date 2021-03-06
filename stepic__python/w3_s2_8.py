﻿import sys

"""
Даны неотрицательные целые числа n, k и массив целых чисел из [0..10^9] размера n. Требуется найти 
k-ю порядковую статистику, т.е. напечатать число, которое бы стояло на позиции с индексом k (0..n-1) 
в отсортированном массиве. Напишите нерекурсивный алгоритм методом "разделяй и властвуй".

Требования к дополнительной памяти: O(n). Требуемое среднее время работы: O(n).

Функцию Partition следует реализовывать методом прохода двумя итераторами в одном направлении от 
начала массива к концу:

Выбирается опорный элемент. Опорный элемент меняется с последним элементом массива.
Во время работы Partition в начале массива содержатся элементы, не бОльшие опорного. 
Затем располагаются элементы, строго бОльшие опорного. В конце массива лежат нерассмотренные элементы. 
Последним элементом лежит опорный.
Итератор (индекс) i указывает на начало группы элементов, строго бОльших опорного.
Итератор j больше i, итератор j указывает на первый нерассмотренный элемент.
Шаг алгоритма. Рассматривается элемент, на который указывает j. Если он больше опорного, то сдвигаем j.
Если он не больше опорного, то меняем a[i] и a[j] местами, сдвигаем i и сдвигаем j.
В конце работы алгоритма меняем опорный и элемент, на который указывает итератор i.

Sample Input:
10 0
3 6 5 7 2 9 8 10 4 1
Sample Output:
1
"""


def get_pivot(array, start_pos, end_pos):
    return (int)((start_pos + end_pos) / 2)

def swap_elem(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def k_elem(arr, n):
    # Выбирается опорный элемент.
    end_pos = len(arr) - 1
    start_pos = 0
    while True:
        pivot = get_pivot(arr, start_pos, end_pos + 1)
        # Опорный элемент меняется с последним элементом массива.
        swap_elem(arr, end_pos, pivot)
        # Во время работы цикла в начале массива содержатся элементы, не большие опорного. 
        # Затем располагаются элементы, строго большие опорного. В конце массива лежат нерассмотренные элементы. 
        # Последним элементом лежит опорный.
        # Итератор (индекс) i указывает на начало группы элементов, строго больших опорного.
        # Итератор j больше i, итератор j указывает на первый нерассмотренный элемент.
        i = 0
        j = 0
        # Шаг алгоритма. 
        # Рассматривается элемент, на который указывает j. Если он больше опорного, то сдвигаем j.
        # Если он не больше опорного, то меняем a[i] и a[j] местами, сдвигаем i и сдвигаем j.
        # Цикл пока не рассмотрены все элементы до последнего (опорного) 
        while j < end_pos:
            if arr[j] > arr[end_pos]:
                j += 1
            else:
                swap_elem(arr, i, j)
                i += 1
                j += 1
        # В конце работы алгоритма меняем опорный и элемент, на который указывает итератор i.
        swap_elem(arr, end_pos, i)
        
        # Если опорный элемент стал на n-ю позицию, тоискомый элемент найден - возвращаем его
        if i == n:
            #print("arr[{0}] = {1} ".format(i, arr[i]))
            return arr[i]
        # Иначе если i > n то надо выбирать искомый элемент слева
        if n < i:
            #start_pos = start_pos # - don't change
            end_pos = i - 1
        # или если i < n то надо выбирать искомый элемент справа
        else:
            start_pos = i + 1
            #end_pos = end_pos # - don't change


def main():
    reader = (list(map(int, line.split(" "))) for line in sys.stdin)
    n, k = next(reader)
    arr = next(reader)
    assert len(arr) == n

    result = k_elem(arr, k)
    print("{0} ".format(result))


def test():
    assert k_elem([3, 6, 5, 7, 2, 9, 8, 10, 4, 1], 0) == 1
    print("**********")
    assert k_elem([3, 0, 2, 1, 5, 4, 21, 4, 6, 5], 2) == 2
    print("**********")
    assert k_elem([0], 0) == 0
    print("**********")
    assert k_elem([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8) == 8
    print("**********")
    assert k_elem(list(reversed([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), 9) == 9
    print("**********")
    assert k_elem([0, 1], 0) == 0
    print("**********")
    assert k_elem([1, 0], 0) == 0



if __name__ == "__main__":
    main()