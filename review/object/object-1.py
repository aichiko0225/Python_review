class Student(object):

    _count = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        Student._count += 1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, score: float):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 使用dir()
print(dir('ABC'))

s = Student('ash', 99)
print('=======  %s  ======' % dir(s))
