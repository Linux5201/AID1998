"""
分组
"""
import re

print(re.search(r'(ab)+','ababababab').group())    # 分组 可以被作为整体操作，改变元字符的操作对象

print(re.search(r'(?P<pig>ab)+','ababababab').group('pig'))    # 命名

print(re.search(r'(王|李)\w{1,3}', '王者荣耀').group())    # 分组 可以被作为整体操作，改变元字符的操作对象

print(re.search(r'(https|http|ftp|file)://\S+', '...: https://www.baidu.com').group())

print(re.search(r'\d{17}(\d|X)', "342222199809161619").group())




