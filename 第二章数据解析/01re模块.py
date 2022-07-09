# Author: by tunan
# Date: 2022/5/27 10:14
# Function:re模块学习

import re

# findall: 匹配字符串中所有的符合正则的内容
# lst = re.findall(r"\d+", "我的电话号码是：1008611，我的老婆的电话是：1001000")
# print(lst)

# finditer: 匹配字符串中所有的内容[返回的是迭代器]
# it = re.finditer(r"\d+", "我的电话号码是：1008611，我的老婆的电话是：1001000")
# for i in it:
#    print(i.group())

s = """
<div class = 'jay'><span id = '1'>狗蛋</span></div>
<div class = 'ji'><span id = '2'>牛二</span></div>
<div class = 'jojo'><span id = '3'>马六</span></div>
<div class = 'tim'><span id = '4'>翠花</span></div>
<div class = 'serena'><span id = '5'>小九</span></div>
"""

# (?/P<group name>re正则表达式) 分组取名 可以单独从正则匹配的内容中进一步提取内容
# compile()预加载一个正则表达式，方便后面的复用
obj = re.compile(r"<div class = '.*?'><span id = '\d+'>(?P<NAME>.*?)</span></div>", re.S) # re.S: 让.能匹配换行符
it = obj.finditer(s)
for i in it:
    print(i.group('NAME'))
lt = obj.findall(s)
print(lt)