# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.


# Срезом
"""
N = int(input('Enter N: '))
K = int(input('Enter shift K: '))

my_list = [i for i in range(N)]

print(my_list)

# my_list_one = my_list[ :K-1]
# my_list_two = my_list[K:]

my_list_end = my_list[K:] + my_list[:K]
print(my_list_end)
"""

# N = int(input('Enter N '))
# K = int(input('Enter K '))

# my_list = (i for i in range(N))
# print(my_list) 

# new_list = []
# for i in range(len(my_list)):
#     if K + i > len(my_list):
#     new_list[i] = my_list[K+i]

# print(my_list)    


my_list = [i for i in range(10)]
print(my_list) 
shift = int(input('Enter shift: '))

for i in range(shift):
    my_list.insert(0, my_list.pop(-1))

print(my_list)    

# my_list = [i**2 for i in range(10) if i  != 4] - 
# - каждое число возводим в квадрат, ктоме 4