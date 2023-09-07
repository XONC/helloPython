import os
import shutil

if __name__ == '__main__':
    with open('test.txt', mode='w', encoding="utf-8") as test:
        test.write('这是一段系统文件系统操作的测试文本')
    # 获取当前文件的路径
    print(os.getcwd())
    # 获取当前目录下的文件和文件夹名，返回一个列表
    print(os.listdir())
    print(os.path.exists("./os_test_folder"))

    # 移动一个文件, 如果没有这个文件，会先创建在移动
    # shutil.move('test.txt', './os_test_dst')
    # 删除路径下的文件，直接删除
    # os.unlink('./test.txt')
    # 删除空文件夹
    # os.rmdir('./os_test_dst')
    # 删除文件夹及其所有子文件夹和文件
    # shutil.rmtree('./os_test_dst')

    # 使用 send2trash 库进行删除，不会直接删除文件，而是会放进回收站

    # os.walk 会搜索路径下全部的包，子包，文件
    path = 'D:\code\project\helloPython\高级python包'
    for folder, sub_folders, files in os.walk(path):
        print(folder)
        print(sub_folders)
        print(files)