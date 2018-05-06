#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello world!!!')
# 格式化

i = 'Hi, %s, you have $%g.' % ('ash', 2000.3)
print(i)

ins = 'Hello, {0}, you have a {1:.1f}'.format('ash', 1233)
print(ins)


list1 = ['Michael', 'Bob', 'Tracy']

print(list1[-1])

str1: str = list1[0]
print(str1)

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')

print(classmates)

# s = input('brith: ')
# birth = int(s)
# if s < 2000:
#     print('00前')
# else:
#     print('00后')

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d)

d.pop('Bob')

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 1, 2, 3, 4])
print(s)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs('A')

# 可变参数

# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

def calc(*numbers):
    sum = 0
    for number in numbers:
        sum += number*number
    return sum


print(calc(1, 2))

numbers = [1, 2, 3]

print(calc(*numbers))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。


def person(name: str, age: int, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}

person('ash', 28, **extra)


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

def person(name, age, *, city, job):
    print(name, age, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：


person('Jack', 24, city='Beijing', job='Engineer')

