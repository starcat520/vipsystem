#coding=utf-8
import requests,sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
def encrypt(key, s):
    b = bytearray(str(s))
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
    return c
def decrypt(key, s):
    c = bytearray(str(s))
    n = len(c) # 计算 b 的字节数
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j+1]
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:
        return b
    except:
        return "failed"
key = 12
r = requests.get('http://scd.free.idcfengye.com/userrd',data={'u':str(encrypt(key, 'a1')),'p':str(encrypt(key, 'a1')),'o':u'1'})
print r.text
if "true" in decrypt(key,eval(r.text)["status"]):
    print("校验成功 此地调用功能")
else:
    print("校验失败 使用调用失败的函数")

#auth(1,2,3)
