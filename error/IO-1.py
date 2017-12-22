import pickle
# 序列化

d = dict(name='Bob', age=20, score=88)

# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
# 如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 首先，我们尝试把一个对象序列化并写入文件：
print(pickle.dumps(d))


# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：


# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：


import json

print(json.dumps(d))

# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 82228)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


