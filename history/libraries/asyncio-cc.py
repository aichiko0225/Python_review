# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

# 用asyncio实现Hello world代码如下：

import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!!!')
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
# loop.close()

# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。

# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

import threading

@asyncio.coroutine
def hello1():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop1 = asyncio.get_event_loop()
tasks = [hello1(), hello1()]
loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()

# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
@asyncio.coroutine
def wget(host: str):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()

    while True:
        line = yield from reader.readline()
        if line == b'\r\n': break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop2 = asyncio.get_event_loop()
tasks2 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop2.run_until_complete(asyncio.wait(tasks2))
# loop2.close()

# 可见3个连接由一个线程通过coroutine并发完成。

# 小结
# asyncio提供了完善的异步IO支持；

# 异步操作需要在coroutine中通过yield from完成；

# 多个coroutine可以封装成一组Task然后并发执行。


# async/await

# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。
# 让我们对比一下上一节的代码：


async def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello2())
