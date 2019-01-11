#coding=utf-8
#适用python2和3
import requests
#客户端无加密 易被破解
username = "调用的用户名"
password = "调用的密码"
r = requests.get('http://127.0.0.1:8081/userrd',data={'u':username,'p':password,'o':'0'})
print(r.text)
if eval(r.text)["status"] == "true":
    print("此地调用功能")
else:
    print("校验失败 使用调用失败的函数")
