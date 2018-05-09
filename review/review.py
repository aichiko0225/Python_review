
from collections import Iterable, Iterator
import os
# 高等特性

# 1. 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

L1 = L[0:3]

print(L1)
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n = 3

for i in range(n):
    r.append(L[i])

print(r)

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：

L[:3]

L2 = list(range(100))

L2[-10:]

# 前10个数，每两个取一个：
l1 = L2[:10:2]

print(l1)
# 所有数，每5个取一个：
l2 = L2[::5]

print(l2)

# 甚至什么都不写，只写[:]就可以原样复制一个list：

l3 = L2[:]

print(l3)


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

T = (1, 3, 4, 5, 6, 6, 7)

t1 = T[:3]

print(t1)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

str1 = 'ABCDEFG'

str2 = str1[:3]

print(str2)

str3 = str1[::2]

print(str3)

# 2. 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：

# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

bool1 = isinstance('abc', Iterable)
print(bool1)

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 3), (2, 4), (5, 6)]:
    print(x, y)

# 3. 列表生成式

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
com = [x * x for x in range(1, 10)]

print(com)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
com1 = [x * x for x in range(1, 10) if x % 2 == 0]

print(com1)

# 还可以使用两层循环，可以生成全排列：
com2 = [m + n for m in 'ABC' for n in 'XYZ']
print(com2)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

com3 = [d for d in os.listdir('.')]
print(com3)

# 列表生成式也可以使用两个变量来生成list：
dic = {'x': 'A', 'y': 'B', 'z': 'C'}
com4 = [k+' = '+v for k, v in dic.items()]

print(com4)

# 最后把一个list中所有的字符串变成小写：

com5 = [v.lower() for v in ['Hello', 'World', 'IBM', 'Apple'] if isinstance(v, str)]
l4 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() if isinstance(s, str) else s for s in l4])
print(com5)


# 4. 生成器
# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

generator1 = (x * x for x in range(1, 10))
print(generator1)

# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
for n in generator1:
    print(n)


def fib(max: int):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


f = fib(6)
print(f)


# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：


while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as identifier:
        print('Generator return value:', identifier.value)
        break

# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

# 5. 迭代器
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象：

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：

isinstance(f, Iterator)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

isinstance(iter([]), Iterator)

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

