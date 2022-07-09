# Author: by tunan
# Date: 2022/6/5 17:08
# Function:

# xpath是在xml文档中搜索内容的一门语言
# html是xml的一个子集

# 安装lxml模块
# xpath解析
from lxml import etree

xml = """
<book>
   <id>1</id>
   <name>刀剑神域</name>
   <price>5</price>
   <nick>鸣人</nick>
   <author>
         <nick id='10086'>佐助</nick>
         <nick id='10010'>小樱</nick>
         <nick class='jay'>周杰伦</nick>
         <nick id='jolin'>蔡依林</nick>
         <div>
              <nick>倒带</nick>
         </div>
   </author>
   <partner>
         <nick id='a'>阿里</nick>
         <nick id='b'>百度</nick>
   </partner>
</book>
"""

tree = etree.XML(xml)
#  result = tree.xpath("/book/name/text()")  # /表示层级关系，当前节点的直接子节点。第一个/是根节点  text()获取文本
#  result = tree.xpath("/book/author//nick/text()")  # //表示当前节点的子孙节点
#  result = tree.xpath("/book/author/*/nick/text()")  # *表示任意的节点，通配符
#  result = tree.xpath("//nick[@id='a']/text()")  # @表示获取属性
result = tree.xpath(".//nick/text()")  # .表示当前的节点

print(result)

