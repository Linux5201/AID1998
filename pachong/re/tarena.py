"""
正则表达式：即文本的高级匹配模式，提供搜索，替换等功能。其本质是由一系列字符和特殊符号构成的字串，这个字串即正则表达式
主要用于字符串的匹配、查找、定位、替换，简单来说就是普通字符和元字符构成的字符串，描述一类字符串规则。
元字符：有特殊含义的符号

"""

import re


# print(re.findall('a', 'abcdefabcd'))
# print(re.findall('com|cn', 'http//www.baidu.com'))        # 满足其中一个条件
# print(re.findall('张.丰', '张三丰，张四丰，张五丰'))           # 任意字符
# print(re.findall('[_#0-9a-z]', 'pd544854f4e8f448e48#'))   # 混合使用
# print(re.findall('[^_#0-9a-z]', 'pP544854f4E8f448G48#'))  # 取反
# print(re.findall('^Jame', 'Jame,hello'))   # ^匹配字符串开头位置
# print(re.findall('^Jame', 'hello，Jame'))   # ^匹配字符串开头位置
# print(re.findall('Jame$', 'hello，Jame'))   # $匹配字符串结尾位置
# print(re.findall('wo*', 'wooooo~~w!'))   # 匹配前面的字符出现0次或多次
# print(re.findall('[a-zA-Z]*', 'How are you?'))   # 匹配前面的字符出现0次或多次
# print(re.findall('[A-Z][a-z]*', 'How are you? Fine Jame'))   # 匹配大写字母开头的单词
# print(re.findall('[A-Z][a-z]+', 'I am good,A boy'))   # +匹配前面的字符出现1次或多次
# print(re.findall('ab?', 'abbbbb,abcdea'))   # ?匹配前面的字符出现0次或1次
# print(re.findall('-?[0-9]+|', '167 -28 29 -8'))   # ?匹配前面的字符出现0次或1次
# print(re.findall('[^ ]+', 'Port-9 Error #404# %@STD'))   # 导出每个单词
# print(re.findall('ab{3}', 'abcdabbbbbbbbbbb'))   # 匹配前面的字符出现n次
# print(re.findall('张.{3}', '张万世界'))   # 匹配前面的字符出现n次
# print(re.findall('ab{2,4}', 'abbcdabbbababbbbb'))   # 匹配前面的字符出现m-n次
# print(re.findall('\d{1,5}', 'Mysql:3306,http:80'))   # \d匹配任意数字字符，\D匹配任意非数字字符
# print(re.findall('\D+', 'Mysql:3306,http:80'))    # \d匹配任意数字字符，\D匹配任意非数字字符
# print(re.findall('\w+', 'server_port = 四个八'))   # \w匹配普通字符，\W匹配非普通字符，普通字符指：数字，字母，下划线，汉字(utf8字符)
# print(re.findall('\w+\s+\w+', 'hello  world'))    # \s匹配空字符，\S匹配非空字符，说明：空字符是指空格、
# # \r回车、\n换行、\t(tab)、\v(垂直制表)、\f换页符
# print(re.findall('\S+', 'hello  world'))          # 匹配两个单词
# print(re.findall('\Ahello', 'hello  world'))      # \A表示开头位置，\Z表示结尾位置
# print(re.findall(r'\bis\b', 'this is a test.'))   # 匹配第二个is  \b表示单词边界，\B表示非单词边界   说明：单词边界是指数字字母（汉字）
# # 下划线与其他字符的交界位置  加r变成原始字符串
# print(re.findall(r'\Bis\b', 'this is a test.'))   # 匹配第一个is   \b表示单词边界，\B表示非单词边界   说明：单词边界是指数字字母（汉字）
# # 下划线与其他字符的交界位置  加r变成原始字符串
# print(re.findall(r'\b\d+\b', '123 65 Num007'))    # 匹配纯数字
# """
# 总结
#     匹配字符
#         .、[....]、[_...]、[^....]、\d、\D、\w、\W、\s、\S
#     匹配重复
#         *、+、?、{n}、{m,n}
#     匹配位置
#         ^ $ \A \Z \b \B
#     其他
#         | () \(转义)
# """

# print(re.findall('-?\d+\.?\d*', "12 -36 28 1.34 -3.8"))    # 匹配每个数字

# print(re.findall('\$\d+', "日薪：$100"))    # 匹配每个数字
# print(re.findall(r'\bis\b', "This is a test"))    # 匹配每
#
# # 二层转义：pyhton字符串先经过自身的转义再转义为正则表达式进行匹配
# print(re.findall('\\\\', "\\"))
# print(re.findall(r'\\', "\\"))   # 在编程语言中，常使用原生字符串书写正则表达式避免多重转义的麻烦,不会进行字符串的转义解析

# # 贪婪模式转换为非贪婪，在其后加上?
# print(re.findall(r'ab{2,4}', 'abbbbbb'))    # 贪婪模式
# print(re.findall(r'ab{2,4}?', "abbbbbb"))   # 非贪婪模式

# s ="[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]"
# print(re.findall(r'\[\w+\]', s))
# print(re.findall(r'\[.+\]', s))
# print(re.findall(r'\[.+?\]', s))


#正则匹配联系

"""
1、匹配一个.com邮箱格式字符串
2、匹配一个密码，8-12位数字字母下划线构成
3、匹配一个数字：正数，负数、整数、小数、分数1/2，百分数45%
4、匹配一段文字中以大写字母开头的单词，注意文字中可能有iPython(不算) H-base(算)
单词可能有 大写字母 小写字母 - _
"""

print(re.findall(r'\w+@\w+\.com', '1466623875@qq.com'))   # 1
print(re.findall(r'\w{8,12}', 'Tedu01234'))   # 2
print(re.findall(r'-?\d+/?\.?\d*%?', '12 -3 3.5 -5.45 42% 1/3'))   # 3
print(re.findall(r'\b[A-Z][-_a-zA-Z]*', 'Hello iPython H-base BSD'))   # 4

















