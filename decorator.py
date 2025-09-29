import time
from unittest import result


# def vaqt_chiqarish():
#     start=time.time()
#     for i in range(1,1000000):
#         print(i)
#     end=time.time()
#     print("ketgan vaqt",end-start,"sekund")
# vaqt_chiqarish()


# def count_dec(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end=time.time()
#         print(end-start)
#     return wrapper
# @count_dec
# def counter():
#     count = 0
#     for i in range(1,100_000_000):
#         count += 1
# counter()


# def count_dec(func):
#     def wrapper():
#         print("azam")
#         func()
#         print("saidov")
#
#     return wrapper
#
# @count_dec
# def hello():
#     print("hello")
# hello()


# import copy
# a=[2,2,3,4,["salom","dunuyo"]]
# b=a
# c=copy.deepcopy(a)
# print(id(a))
# print(id(c))

# import copy
# a = [[1, 2, 3], [4, 5, 6]]
# b=copy.copy(a)
# c=copy.deepcopy(a)
# a[0][0] = 99
# print(a)
# print(b)
# print(c)

# def count_dec(func):
#     def wrapper():
#         print("azam")
#         func()
#         print("saidov")
#
#     return wrapper
#
# @count_dec
# def hello():
#     print("hello")
# hello()