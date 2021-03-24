from Diapazon import *

def get_obj(array):
    diap_arr = []
    i = 0
    while (i < len(array)-1):
        temp = Diapazon(array[i] , array[i+1])
        if temp.start:
            diap_arr.append(temp)
        i += 2
    return diap_arr

def check(array):
    for i in array:
        print(i)
    print('-'*20)

def sort_Diap(array):
    sorted = False
    while (not sorted):
        sorted = True
        i = 0
        while (i < len(array)-1):
            if (array[i].start > array[i+1].start):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                sorted = False
            i += 1
    return array

def union_diap(array):
    temp_array = []
    temp = array[0]
    i = 1
    while (i < len(array)):
        a = temp
        temp = a.union(array[i])
        if not temp:
            temp_array.append(a)
            temp = array[i]
        i += 1
    if temp:
        temp_array.append(temp)
    else:
        temp_array.append(array[-1])
    return temp_array

def cut_lesson(array , lesson):
    #обрезка слева
    for i in range(len(array)):
        if (array[i].end > lesson[0]):
            break
    array = array[i:]
    if array[0].start < lesson[0]:
        array[0].start = lesson[0]
    
    #обрезка справа
    need_cut = False
    for i in range(len(array)):
        if (array[i].start >= lesson[1]):
            need_cut = True
            break
    if (need_cut):
        array = array[:i]
        
    if array[-1].end > lesson[1]:
        array[-1].end = lesson[-1]
    return array

def union_array(array1, array2):
    realLessonTime = []
    for i in array1:
        for j in array2:
            result = i.unionMaxima(j)
            if result == -1:
                continue
            if result == -2:
                break
            realLessonTime.append(result)        
    return realLessonTime

def get_time(array):
    summ = 0
    for i in array:
        summ += i
    return summ