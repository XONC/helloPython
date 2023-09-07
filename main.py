# 从库中导入 shuffle 随机函数
from random import shuffle
from random import randint
import string
import timeit
# pip install 安装包，类似于npm
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hi , {name}'.format(name = name))
    print('Hi,{name}')
    a = 'abcdfvgt'
    b = a[3:]
    c = a[:]
    d = a[:3]
    print(b)
    print(c)
    print(d)
    e = 'this is {}'.format(name)
    f = 100 / 777
    print(e)
    print(f)
    print('this float is {r:24.12f}'.format(r = f))

    g = {
        'test': 1,
        'test1': 2,
        'test3': 3,
        'test4': 3,
        'test2': 2,
    }

    print(g)

    h = open('myfile.txt','w',encoding='utf-8')
    h.write('this is firstLine\nthis is secendLine')
    h.close()

    # 会自动关闭
    # 读取模式 无法使用write方法
    with open('myfile.txt',mode='r') as j:
        # print(j.read()) 读取全部
        print(j.readline()) # 读取一行，参数表示行内字符
        # j.write('text')

    with open('myfile.txt', mode='a') as k:
        k.write('text') # 会在最后一行添加字符
        # print(k.read()) # append 模式无法读取

    with open('myfile.txt',mode='w') as l:
        l.write('text')
        # print(l.read()) write 模式 无法读取

    with open('myfile2.txt',mode='w',encoding='utf-8') as q:
        q.write('text1')

    # 与 或 非
    print(1 == 1 and 2 == 2)

    print(1 != 1 or 3 != 2)

    print(not 1 != 1)

    # if else
    w = True
    if w:
        print('True')
    elif w == '11':
        print('11')
    else:
        print('False')

    # 循环
    print('循环')
    e = [1,2,3,4]
    for item in e:
        print(item)
    # 循环元组
    print('循环元组')
    r = [(1, 2), (1, 3), (3, 4)]
    for (a,b) in r:
        print(a)
        print(b)
    print('循环元组v1')
    for a,b in r:
        print(a)
        print(b)
    print('循环字典')
    t = {'key1':1,'key2':2,'key3':3}
    for key,value in t.items():
        print(key)
        print(value)
    for value in t.values():
        print(value)

    # while, break, continue, pass
    y = 0
    while y < 10:
        y += 1
        print(y)
    # else 可写可不写
    else:
        print('退出循环')

    while y < 10:
        pass # 由于python 没有没有{}，所以如果这里啥都不写，则无法标记空语句，所以有pass关键字来标记

    # 常用方法
    # range: 0到10，步长2
    print(list(range(0, 10, 2)))
    for i in range(3):
        print(i)
    # zip 将三个数组内的元素，按照最短长度合并成一个元组的数组
    u = range(3)
    i = ['a', 'b', 'c']
    o = ['ads', 'b', 'c']
    for item in zip(u, i, o):
        print(item)
    # 枚举 具有索引的元组
    for item in enumerate(i):
        print(item)
    # in 关键字
    print('a' in i)
    print('a' in 'abv')
    print('a' in {'a': 'key'}) # True
    print('a' in {'b': 'as'}) # False
    print('a' in {'b': 'a'}.values()) # True
    # min max 关键字
    print(max(i))
    print(min(i))
    # shuffle 打乱列表
    print(shuffle(i)) # None 不返回任何东西
    print(i)
    # randint 随机返回中间数
    print(randint(0, 100))
    # input 输入函数
    # result = input('Enter value: ')
    # print(result)
    # type 类型检测函数
    print(type(i))
    # int 整形转换函数
    print(int('1'))
    # float 浮点转换函数
    print(float(1))

    # 习题
    st = 'Print only the words that start with s in this sentence'
    print([item for item in st.split(' ') if item[0].lower() == 's'])
    print([item for item in range(0,10) if item % 2 == 0])
    print([item for item in range(1,50) if item % 3 == 0])
    print([item for item in st.split(' ') if len(item) % 2 == 0])
    print(set(item[0] for item in st.split(' ')))
    p = []
    for item in range(1,100):
        if item % 5 == 0 and item % 3 == 0:
            p.append({item: 'FizzBuzz'})
        elif item % 3 == 0:
            p.append({item: 'Fizz'})
        elif item % 5 == 0:
            p.append({item: 'Buzz'})
    print(p)
# 一个关于猜球的游戏
def guess_ball():
    a = ['0', '', '']
    shuffle(a)
    index = int(input('请输入号码：'))
    while index not in [0, 1, 2]:
        index = int(input('请输入【0，1，2】'))
    if a[index] == '0':
        print(f'猜中了！{a}')
    else:
        print(f'猜错了！{a}')
# 多参数传递
def many_args(*args):
    # args 会将参数处理成一个元组数组
    pass
def many_kwargs(**kwargs):
    # kwargs 会将参数处理成一个字典
    pass
def many_args_kwargs(*args, **kwargs):
    # 参数顺序必须按照这样
    pass
# 偶数返回更小，奇数返回更大
def even_lesser_and_odd_greater(a,b):
    if(a%2 == 0 and b%2 ==0):
        return max(a,b)
    else:
        return min(a,b)
# 字符串首字符相同返回true,否则false
def animal_crackers(str):
    item = str.lower().split(' ')
    return item[0][0] == item[1][0]
# 传入两个整数，整数和为20返回真
def makes_twenty(a, b):
    return sum(a, b) == 20 or a == 20 or b == 20
# 输入一个字符串，将第一个字符和第四个字符大写 capitalize() 首字符大写
def old_macdonald(text):
    first_helf = text[:3]
    secend_helf = text[3:]
    return first_helf.capitalize() + secend_helf.capitalize()
# 反转句子
def master_yoda(text):
    wordlist = text.split()
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist)
# 传入一个值，200 - n 之后的绝对值在 100 - 200 之间
def almost_there(n):
    return (abs(200 - n) > 100) and (abs(200 - n) < 200)
# 传入一个列表，如果相邻元素为 3，3 则返回true. 例：【1,3,3】true,【3,1,3】false
# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#         if(nums[i] == 3 and nums[i + 1] == 3):
#             return True
#     return False
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if(nums[i:i+2] == [3,3]):
            return True
    return False
# 传入一个字符串，将每个字符串的字母复制三次，返回格式化后的字符串
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result
# 传入三个1到11之间的整数，如果他们的和小于等于21，则输出，如果他们的和大于21,且小于31，且有一个值为11，则将和减10返回，如果他们的和大于21，则返回 BUST
def blackjack(*args):
    result = sum(args)
    if result <= 21:
        return result
    elif 11 in args and result <= 31:
        return result - 10
    else:
        return 'BUST'
# 传入一个数组，忽略 6 到 9 之间的元素，返回其他元素的和
def summer_69(arr):
    result = 0
    canSum = True
    if len(arr) == 0:
        return 0
    for item in arr:
        if item == 6:
            canSum = False
        elif item == 9:
            canSum = True
        else:
            if canSum:
                result += item

    return result
# 传入一个数组，如果数组内的值有 0，0，7，则为true
# def spy_game(arr):
#     spy = ''
#     for item in arr:
#         if item == 0 and spy[:2] != '00':
#             spy += str(item)
#         elif item == 7 and spy[:2] == '00':
#             spy += str(item)
#             return True
#     return False
def spy_game(arr):
    code = [0,0,7,'x']
    for item in arr:
        if item == code[0]:
            code.pop(0)
    return len(code) == 1
# 获取所有素数
def count_primes(nums):
    # 0,1 不是素数
    # 2,3,5,7,11,13,17,23
    if nums < 2:
        return 0
    primes = []
    for x in range(2, nums+1):
        isPrime = True
        for y in primes:
            if x%y != 0:
                isPrime = True
            else:
                isPrime = False
                break
        if isPrime:
            primes.append(x)

    print(primes)
    return len(primes)
# lambda 表达式
def lambda_test():
    print(list(map(lambda num: num**2, [1,2,3,4])))
    print(list(filter(lambda num: num%2 == 0, [1,2,34,4])))
# 圆得面积
def vol(rad):
    return 3/4 * (3.14) * (3**3)
# 检查一个数在给定得范围内的高低
def ran_check(num, low, high):
    return num in range(low,high)
# 计算一句话中的大写字母和小写字母
def up_low(s):
    d = {'upper': 0,'lower': 0}
    for word in s:
        if word.isupper():
            d['upper'] += 1
        elif word.islower():
            d['lower'] += 1
        else:
            pass
    return d
# 数组去重
def unique_list(lst):
    return list(set(lst))
# 数组内元素相乘
def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
# 检查元素是否回文
def palindrome(s):
    return s == s[::-1]
# 检查句子中是否包含特定短语
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str = str1.replace(' ', '')
    str = str.lower()
    str = set(str)
    return str == alphaset
# 异常
def except_test():
    while True:
        try:
            myInput = int(input('请输入一个数字：'))
        except OSError:
            print('系统错误')
            continue
        except:
            print('其他错误')
            continue
        else:
            print('无错误时触发')
            break
        finally:
            print('无论如何都会触发')
# pylint 单元测试

# 直接执行时调用
if __name__ == '__main__':
    print_hi('PyCharm')
    # guess_ball()
    print(animal_crackers('xlp xw'))
    print(old_macdonald('macdonald'))
    print(master_yoda('i am bool'))
    print(almost_there(150))
    print(has_33([3, 1, 3]))
    print(has_33([1, 3, 3]))
    print(paper_doll('hello'))
    print(blackjack(10,10,10))
    print(summer_69([1,3,4,5,6,7,8,9,2]))
    print(spy_game([1,2,7,3,0,223,0,32,7]))
    print(count_primes(100))
    print(lambda_test())
    print(vol(4))
    print(ran_check(5,2,10))
    print(up_low('this is My Name'))
    print(unique_list([1,1,1,2,3,3,4,5]))
    print(multiply([2,3,-5]))
    print(palindrome('sassas'))
    print(except_test())
# 被import时调用
else:
    pass