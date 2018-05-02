# 函数式编程

# 函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。
# 函数就是面向过程的程序设计的基本单元。

# 而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

# 我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

# 在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

# 而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

# 对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。s

from functools import reduce

def add(x, y, f):
    return f(x) + f(y)

print(add(-2, 30, abs))

def f(x: int):
    return x * x

arr1 = map(f, [1, 2, 3, 4, 5, 6.6])
print(list(arr1))

def add1(x, y):
    return x * 10 + y

print(reduce(add1, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x*10+y, [1, 2, 3, 4, 5]))


def is_odd(n):
    return n%2 == 1

arr2 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(arr2)

# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum)
print(lazy_sum())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# f1, f2, f3 = count()

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count1():
    def f(j):
        return lambda: j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

arr3 = count1()

for f in arr3:
    print(f())


# 匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

# 装饰器 Decorator
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。


# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print('call %s():', func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()


def log_text(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_text('execute')
def now1():
    print('2015-3-25')


now1()

# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


def test1(func, x=None):
    if x != None:
        func('ash')

test1(lambda x: print(x), 233)


