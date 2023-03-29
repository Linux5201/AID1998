"""
flags,pr
flags扩展功能演示
"""
import re

s = """Hello
北京
"""


# 只能匹配ASCII编码
regex = re.compile(r'\w+',flags=re.A)

l = regex.findall(s)
print(l)

# 不区分大小写
regex = re.compile(r'[a-z]+',flags=re.I)
l = regex.findall(s)
print(l)

# 使.可以匹配换行
regex = re.compile(r'.+', flags=re.S)
l = regex.findall(s)
print(l)

# 使^,$ 匹配每一行开头结尾位置
regex = re.compile(r'^北京', flags=re.M)
l = regex.findall(s)
print(l)

# 给正则表达式添加注释
pattern = r"""\w+  # hello
\s+ # 匹配换行
\w+ # 北京
"""
regex = re.compile(pattern, flags=re.X)
l = regex.findall(s)
print(l)


# 满足不区分大小写以及，给正则表达式添加注释
pattern = r"""[a-z]+  # 不区分大小写
"""
regex = re.compile(r'[a-z]+', flags=re.I | re.X)
l = regex.findall(s)
print(l)


