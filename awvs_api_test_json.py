#仅仅test，可以加个队列,任务放几个,做个监控,任务,扫描全网,总能出几个吧..api得json数据代表得意思,还需另查文档
#设置登陆得邮箱,是邮件发送到得邮箱..用自己得邮箱做登陆用户名

#smtp:smtp.163.com
#port:465
#ssl
#username ****@163.com
#passwd: 授权码
#不知道为啥只显示高危几个,中危险几个,可能需要自己写个hook,监控,扫描结果
#--coding:utf-8


import json
import ssl
import urllib.request
import os
ssl._create_default_https_context = ssl._create_unverified_context
host='desktop-kddqmbb:3443'
api_key='1986ad8c0a5b3df4d7028d5f3c06e936c460c0c8a56ab40369ac92f9201e51100'
def create_tagert():
    url="https://"+host+"/api/v1/targets"
    headers = {"X-Auth": api_key, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    values = {
        'address': 'http://192.168.4.80/sqli/Less-1/?id=1',
        'description': 'this is json tssst',
        'criticality': 10,
    #     此处criticality  对应得0，10，20，30 分别是Business Criticality   低中
    #此处得json数据应该是...木有去找api文档

    }
    data = bytes(json.dumps(values), 'utf-8')
    request = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    return html
# zz=create_tagert()
# print (zz)

'''
{
 "address": "http://192.168.4.80/sqli/Less-1/?id=1",
 "criticality": 10,
 "description": "this is json tssst",
 "type": "default",
 "target_id": "a1f99109-aa68-4bbd-bbba-1436581ca612"
}
'''

def start_target(target_id):
    # if target_id==None:
    #     target_id='a1f99109-aa68-4bbd-bbba-1436581ca612'
    #     profile_id=0
    # if schedule==None:
    #     schedule=0
    url = 'https://' + host + '/api/v1/scans'

    headers = {"X-Auth": api_key, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    values = {
        #这三个值,有点问题..不知道对应得是哪三个..
        'target_id': target_id,
        'profile_id': "11111111-1111-1111-1111-111111111111",
        'schedule': {"disable": False, "start_date": None, "time_sensitive": False},
    }
    data = bytes(json.dumps(values), 'utf-8')
    request = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    return html

cc=start_target('a1f99109-aa68-4bbd-bbba-1436581ca612')
print(cc)
##https://blog.csdn.net/sinat_25449961/article/details/82985638
#test东西出来了,有空研究下扫描器得其他绘制模块
#相关
