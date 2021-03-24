def task(array):
    if type(array) != list:
        return None
    counter = 0
    for i in array:
        if (i == 0):
            return counter
        counter+=1
    return None

# Сложность алгоритма O(n) - линейная
# Можно реализовать и через list.index() , но тогда может вернуться Error



