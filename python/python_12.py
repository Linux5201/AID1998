"""
通用操作  str
数学运算符
"""

str01 = "悟空"
str02 = "八戒"
#字符串拼接
str03 = str01+str02
#字符串累加
str01 +=str02
print(str03)
print(str01)
#字符串翻倍
print(str02 * 3)
str02 *= 5
#依次比较两个容器中元素，一旦不同则返回比较结果，比较编码值
print("a悟空">"b八戒")

"""
成员运算符
"""
print("大圣" in "我叫齐天大圣")
#必须连着，必须按照顺序


#索引
#切片
"""
-6-5-4-3 -2 -1
我 是 齐 天 大 圣
0  1 2  3  4  5
正向索引与反向索引
访问容器元素
"""
message = "我是齐天大圣"
print(message[0])
print(message[-1])

#切片可以定一片 容器[(开始索引）:(结束索引)(:步长）]，开始值默认是开头，结束值默认是结尾

print(message[0:2])  #我是
print(message[:2])  #我是
print(message[-2:])  #大圣
print(message[:])  #全部
#大天齐
print(message[-2:-5:-1])
#全部倒着
print(message[::-1])







