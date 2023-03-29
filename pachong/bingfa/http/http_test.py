"""
http使用tcp传输
响应行  响应头  空行  响应体
"""

from socket import *

s = socket()
s.bind(('0.0.0.0', 8000))
s.listen(3)


c, addr = s.accept()
print("Connnect from", addr)
data = c.recv(4096)   # 接收http请求
print(data)

# 将数据组织为响应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello World</h1>
"""

c.send(response.encode())   # 发送响应内容
c.close()
s.close()







