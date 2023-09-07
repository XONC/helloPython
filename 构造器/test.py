# 经典斐波那契数列
import random


def create_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        # 将a暂存在内存中
        yield a
        a, b = b, a+b

# 求一个数的平方
def gensquares(n):
    for i in range(n):
        yield i**2

# 生成给定的数之间的随机数
def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

# 将字符串转化为可迭代对象
def str_to_iter(s):
    return iter(s)

if __name__ == "__main__":
    # list 内部可以对 yield 进行迭代
    print(list(create_fibon(10)))

    # 获取暂存在内存中全部a
    fibon = create_fibon(10)
    # 使用next依次打印
    print(next(fibon))
    print(next(fibon))
    print(next(fibon))

    iter_list = [1,2,3,4]
    # 可以使用iter将可迭代对象里的值存入内存，然后使用next进行依次打印
    iter_list_val = iter(iter_list)
    print(next(iter_list_val))
    print(next(iter_list_val))
    print(next(iter_list_val))

    print(list(gensquares(10)))
    print(list(rand_num(1, 10, 10)))