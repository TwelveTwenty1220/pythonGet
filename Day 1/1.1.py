# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from urllib.request import urlopen

def main(url) :
    resp=urlopen(url)
    print(resp.read().decode('utf-8'))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
      url='http://www.baidu.com'
      main(url)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
