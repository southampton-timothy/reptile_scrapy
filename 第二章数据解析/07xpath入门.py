# Author: by tunan
# Date: 2022/6/6 12:40
# Function:

from lxml import etree

tree = etree.parse("test.html")
#  result = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的顺序从1开始数的,[]表示序号筛选
result = tree.xpath("//ol/li/a[@href='bus']/text()")  # [@xxx=xxx]表示属性的筛选 //开头表示根节点的所有子孙节点(类似于相对路径，省去开头的路径)
print(result)
ol_li_list = tree.xpath("//ol/li")
for i in ol_li_list:
    print(i.xpath("./a/text()"))  # ./表示相对路径，.当前节点
    print(i.xpath("./a/@href"))   # 拿到属性值@

print(tree.xpath("//ul/li/a/@href"))

print(tree.xpath("/html/body/div[1]/@class"))