def get_list() -> list:
    return list(range(0, 1_000_000, 2))

print(get_list)
"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:

    """
        find_target -> YOUR_CODE
    """
    
def find_target(list,target):

    low = 0
    nigh = len(list) -1
    target_res = False

    while low <= nigh and  not target_res:
        middle = (low + nigh) // 2
        gus = list[middle]
        if gus == target:
            target_res = True
            return target_res
        if gus > target:
            nigh = middle -1
        else:
            low = middle + 1
    return target_res 

list = [1,3,5,45,47,50,67,77]
tar = 3
                     
print(find_target(list,tar))              

"""  что такое Binary Search? - Это Двоичный (бинарный) поиск  известен как метод деления пополам —
классический алгоритм поиска элемента в отсортированном массиве (векторе)
использующий дробление массива на половины


Зачем нужен Binary Search?- бинарный поиск нужно чтобы найти искомого  элемента в отсортированном
массиве 


Принцип работы Binary Search - 1)Сортируем массив данных.
2)Делим его пополам и находим середину.
3)Сравниваем срединный элемент с заданным искомым элементом.
Если искомое число больше среднего — продолжаем поиск в правой части массива (если он отсортирован по возрастанию):
делим ее пополам, повторяя пункт 3.Если же заданное число меньше —
алгоритм продолжит поиск в левой части массива, снова возвращаясь к пункту 3.

"""
    


        