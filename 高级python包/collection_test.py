from collections import namedtuple
from collections import defaultdict
from collections import Counter

def test():
    # 命名元祖，可以通过键值的方式去使用元祖,实际是创造了一个Dog类
    Dog = namedtuple('Dog', ['name', 'sex', 'age'])
    summary = Dog('wx', 1, 12)
    print(summary)

    # 默认字典, 可以设置字典的默认值, 参数为一个函数
    dict_test = defaultdict(lambda: 0)
    dict_test['name'] = 100
    print(dict_test)
    print(dict_test['age'])

    # Counter 本身可以收集相同的数组元素，返回一个Counter对象
    list_a = [1,1,1,1,2,2,3,44,5,5,5,2,6,6]
    c = Counter(list_a)
    print(c)
    # 使用list去重
    print(list(c))
    # 使用本身的 most_common 可以将对象转变成 包含元组的列表
    print(c.most_common(len(c)))
    # values 获取值列表
    print(list(c.values()))
    # 将对象转变为字典
    print(dict(c))
    # 清空Counter里的内容
    c.clear()
    print(c)


if __name__ == '__main__':
    test()
