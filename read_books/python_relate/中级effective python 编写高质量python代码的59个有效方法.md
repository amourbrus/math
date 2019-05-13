python 3.4
出版时间: 2016年1月第一版
阅读时间：20190430
### 第1章 用pythonic方式思考
#### 第1条：确认自己所用的python版本
#### 第2条：pep8
#### 第3条：bytes,str,unicode
#### 第4条：用辅助函数取代复杂的表达式
#### 第5条：切割序列的方法
省掉开头，省掉结尾，倒序[::-1],[:]不会有indexerror
#### 第6条：不要同时指定 start,end,stride
#### 第7条：用列表推导取代map，filter
#### 第8条：不要使用含有两个以上表达式的列表推导


#### 第9条：用生成器表达式来改写数据量较大的列表推导
更快、更少内存
```python
id = (len(x) for x in open('/tmp/file.txt'))  # 注意该迭代器是有状态的，用过一轮后不要反复使用
print(next(id))
roots = ((x, x**0.5) for x in id)
```
#### 第10条：尽量用enumerate 取代range
```python
for i in range(len(xx_list))  
for i, x in enumerate(xx_list)
```
#### 第11条：用zip同时遍历两个迭代器
```python
names = ['cecilia', 'lise', 'Marie']
letters = [len(n) for n in names]
for name, count in zip(names, letters):  # 生成器
  if count>max_letters:
    longest_name = name
    max_letters = count
```
#### 第12条：不要在for和while循环后写else块
为了可读性，不建议使用。该else是循环没有break，return才执行，用and更好理解
#### 第13条：合理使用try/except/else/finally中的每个代码块
else块可以缩减try中的代码量，没有异常则执行else,finally无论是否发生异常，都执行(如清理工作)
### 第2章 函数
#### 第14条：尽量用异常来表示特殊情况，而不要返回None
#### 第15条：了解如何在闭包里使用外围作用域中的变量
```python
def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)
  values.sort(key=helper)
numbers = [8,9,6,5,3,4,7,6,2]
group = {2,3,5}
sort_priority(numbers, group)
print(numbers)
```
#### 第16条：考虑用生成器来写直接返回列表的函数
#### 第17条：在参数上面迭代时要小心--如果参数是迭代器
判断某个值是迭代器还是容器，可以拿该值为参数，两次调用iter函数，若结果相同，则是迭代器
#### 第18条：用数量可变的位置参数减少视觉杂讯
注意：对生成器使用*操作符，可能导致程序耗尽内存并崩溃
#### 第19条：用关键字参数来表达可选的行为
#### 第20条：用None和文档字符串来描述具有动态默认值的参数
如果函数默认参数赋值是某个值 如：default={},time=datetime.now(),这些只会执行一次，如果调用两次，则default会生成一个字典
#### 第21条：用只能以关键字形式指定的参数来确保代码明晰
在python3中，以*号标志位置参数到此终结，之后的参数只能以关键字形式来指定
```python
def safe_division(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
  pass
```
### 第3章 类与继承
善用类和继承就可以写出易于维护的代码

#### 第22条：尽量用辅助类来维护程序的状态，而不要用字典和元组
如果容器中包含简单又不可变的数据，可以先使用namedtuple来表示
#### 第23条：简单的接口应该接受函数，而不是类的实例
```python
increments = [('red', 5), ('blue', 17)]
class BetterCounMissing(object):
    def __init__(self):
        self.added = 0
    def __call__(self):
        self.added += 1
        return 0
counter = BetterCounMissing()
counter()
callable(counter)

from collections import defaultdict
counter = BetterCounMissing()
current = {'green': 12, 'blue': 3}
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
counter.added
```
直接传入函数，而不是传类的实例
通过__call__方法，可以使类的实例能够像普通的python函数那样得到调用
#### 第24条：以@classmethod形式的多态去通用的构建对象
在python中，一个类只有一个构造器，即__init__方法
通过@classmethod机制，可以用一种与构造器相仿的方式来构造类的对象
#### 第25条：用super初始化父类
#### 第26条：只在使用Mix-in组件制作工具类时进行多重继承
#### 第27条：多用public属性，少用private属性
#### 第28条：继承collections.abc以实现自定义的容器类型
### 第4章 元类及属性
metaclass 模糊地描述了一种高于类，而又超乎类的概念。简单说，就是我们可以把python的class语句转译为元类，并令其在每次定义具体的类时，提供独特的行为
这些机制只适合用来实现那些广为人知的python编程范式，避免太古怪
#### 第29条：用纯属性取代get和set方法
对比其他语言来说的
#### 第30条：用@property来代替属性重构
#### 第31条：用描述符来改写需要复用的@property方法
#### 第32条：用__getattr__和__getattribute__和__setattr实现按需生成的属性
#### 第33条：用元类来验证子类
#### 第34条：用元类来注册子类
#### 第35条：用元类来注解类的属性
### 第5章 并发及并行
并发 concurrency seemingly
并行 parallelism actually
#### 第36条：用subprocess模块来管理子进程
#### 第37条：可以用线程来执行阻塞式I/O，但不要用它做平行计算
由于GIL
#### 第38条：在线程中使用Lock来防止数据竞争
固然同一时刻只有一个python线程得以运行，但是当这个线程正在操作某个数据结构时，其他线程可能会打断它，如果其他线程也操作这个数据，那就会引发危险的结果
#### 第39条：用Queue来协调各线程之间的工作
阻塞式队列操作(线程安全)
#### 第40条：考虑用协程来并发地运行多个函数
线程缺点：
1. 为了确保数据安全，需要工具来协调这些线程
2. 线程需要占用大量的内存，每个正在执行的线程大约占用内存8M
3. 线程启动开销大，拖慢速度
协程的实现方式，是对生成器的一种扩展，启动的开销与调用函数相近。占用不到1KB的内存
#### 第41条：考虑用concurrent.futures来实现真正的平行计算
concurrent.futures的ProcessPoolExecutor, 不用mutiprocessing的那些高级功能
### 第6章 内置模块
#### 第42条：用functools.wraps定义函数修饰器
#### 第43条：考虑用contextlib和with语句来改写可复用的try/finally
#### 第44条：用copyreg实现可靠的pickle操作
#### 第45条：用datetime模块处理本地时间而不是time模块
不同时区之间，datetime和pytz配合使用。开发者总是该先把时间表示成UTC格式
#### 第46条：使用内置算法和数据结构
1. 双向队列 collections.deque FIFO
fifo = deque()
fifo.append(1)  # producer
x = fifo.popleft()  # consumer
2. 有序字典 collections.OrderedDict
3. 带有默认值的字典 collections.defaultdict
4. 堆队列 优先级队列 heapq 模块提供了heappush,heappop,nsmallest等函数可以在标准的list类型中创建堆结构
a = []
heappush(a, 5)
heappush(a, 3)
5. 二分查找 bisect模块的bisect_left等函数
x = list(range(10**6))
i = x.index(991234)  # 所耗时间与队列长度呈线性
i = bisect_left(x, 991234)  # 对数
6. 与迭代器有关的工具 itertools模块
分三类：
- 能够把迭代器连接起来的函数：chain, cycle, tee, zip_longest
- 能够从迭代器中过滤元素：islice,takewhile, dropwhile, filterfalse
- 能够把迭代器中的元素组合起来的函数：product, permutations,conbination
#### 第47条：在重视精确度的场合，应该使用decimal
#### 第48条：学会安装由python开发者社区所构建的模块 pypi
### 第7章 协作开发
#### 第49条：为每个函数、类和模块写文档字符串
#### 第50条：用包来安排模块，提供稳固的API
谨慎使用 import *
#### 第51条：为自编的模块定义根异常，以便将调用者与API相隔离
#### 第52条：用适当的方式打破循环依赖关系
#### 第53条：使用虚拟环境
### 第八章 部署
#### 第54条：用模块级别的代码来配置不同的部署环境 conf.cnf
#### 第55条：通过repr字符串来输出调试信息
#### 第56条：用unittest来测试全部代码
还有一种常用的方法是mock
#### 第57条：考虑用pdb实现交互调试
#### 第58条：先分析性能再优化
#### 第59条：用tracemalloc来掌握内存的使用情况
