import sys
from collections import Iterable
import os

print('6666')

i = sys.api_version
print(i)

if __name__ == "__main__":
    print('hello world!')

# name = input('please enter your name: ')

# print('hello', name)

str1 = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(str1)

# 一些基础知识的复习

classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)
print(classmates)
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
classmates[-1]
# 以此类推，可以获取倒数第2个、倒数第3个：
classmates[-2]

classmates.append(233)

print(classmates)

t2 = (1, 2)

t1: (str, int) = ('23', 333)
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

for name in classmates:
    print(name)
    pass
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
number = dict1.get('ash', -33)
print(number)

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。



# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

if isinstance('abc', Iterable):
    print('TRUE')



# 列表生成式

arr1 = [x * x for x in range(1, 11)]
print(arr1)

arr2 = [x * x for x in range(1, 11) if x%2 == 0]
print(arr2)

arr3 = [m + n for m in 'ABC' for n in 'XYZ']
print(arr3)

arr4 = [d for d in os.listdir('.')]
print(arr4)



# 生成器 

generator = (x * x for x in range(1, 11))
print(generator)

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def fib(max: int):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib(6)
print(f)

for n in f:
    print('fib --', n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 小结
# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。



from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
