from datetime import datetime

now = datetime.now()

print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)

print(dt)

print(dt.timestamp())


print(datetime.fromtimestamp(dt.timestamp()+ 2000))


t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间


cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x, p.y)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

# 如果要保持Key的顺序，可以用OrderedDict：


d = dict([('a', 1), ('b', 2), ('c', 3)])

print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = True if key in self else False
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
    
# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
counter = Counter()

for ch in 'programming':
    counter[ch] = counter[ch] + 1

print(counter)


# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。

# 