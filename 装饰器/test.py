# 装饰器本质是一个函数
def new_decorator(original_func):

    def wrap_func():
        print("一些额外的代码，在执行参数函数之前")

        original_func()

        print("一些额外的代码，在执行参数函数之后")

    return wrap_func


# 当我执行test_func 时，实际执行的是new_decorator
@new_decorator
def test_func():
    print("这是test_func")


if __name__ == "__main__":
    test_func()
