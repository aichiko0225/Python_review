# 在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

# 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，
# 这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。

# 使用模块有什么好处？

# 最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。
# 当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。

# 使用模块还可以避免函数名和变量名冲突。
# 相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
# 但是也要注意，尽量不要与内置函数名字冲突。点这里查看Python的所有内置函数。

# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

from mycompany.abc import add, greeting

print(add(1, 4, lambda x: x*10))

print(greeting('ash-2'))



