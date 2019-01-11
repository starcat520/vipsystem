#coding=utf-8
import requests
def encrypt(key, s):
    b = bytearray(str(s).encode("gbk"))
    n = len(b) # 求出 b 的字节数
    c = bytearray(n*2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码
        c[j] = c1
        c[j+1] = c2
        j = j+2
    return c.decode("gbk")
key = 12
r = requests.get('http://127.0.0.1:8081/userrd',data={'u':encrypt(key, 'test'),'p':encrypt(key, 'test'),'o':'1'})
print r.text
if eval(r.text)["status"] == "true":
    print("此地调用功能")
else:
    print("校验失败 使用调用失败的函数")
