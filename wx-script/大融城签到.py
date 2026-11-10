from datetime import datetime
import time

import requests
import os
import hashlib

# 微信小程序大融城签到,可以抵扣停车费


APPID = 'wx24d80b0b74d12b46'   #大融城app的id
YYB_SERVER = os.environ.get("YYB_SERVER")  # 自己建立yyb_go的网址
appid ='0af4654470625f46bd07b9a2c432b975' #这个每个人一不一样不知道，抓Token/Login这个链接查看

def hex_md5(txt):
    md5 = hashlib.md5()  # 创建一个md5对象
    md5.update(txt.encode('utf-8'))  # 使用utf-8编码数据
    return md5.hexdigest()  # 返回加密后的十六进制字符串

def get_score(token):
    headers = {
        "Host": "memberv5.imixpark.com",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "Authorization": "Bearer " + token,
        "buildingid": "80014",
        "xweb_xhr": "1",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541f0d) XWEB/25799",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx24d80b0b74d12b46/182/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url = 'https://memberv5.imixpark.com/fzapi/ApiScrmCusApp/IMIX/Sign/QueryBsActivitySignInfoIMIX'
    data = {}
    response = requests.post(url, headers=headers, json=data)
    score = response.json()['data']['memberinfo']['member_current_bonus']

def get_current_time_23():
    # 当前 Unix 时间戳，单位：纳秒
    ns = time.time_ns()

    # 拆成：整秒 + 秒内纳秒
    sec, nano = divmod(ns, 1_000_000_000)

    # 转成本地时间
    dt = datetime.fromtimestamp(sec)

    # 年月日时分秒 + 9位纳秒
    return dt.strftime("%Y%m%d%H%M%S") + f"{nano:09d}"

def sign(token):
    headers = {
        "Host": "memberv5.imixpark.com",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "Authorization": "Bearer "+token,
        "buildingid": "80014",
        "xweb_xhr": "1",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541f0d) XWEB/25799",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx24d80b0b74d12b46/182/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url = 'https://memberv5.imixpark.com/fzapi/ApiScrmCusApp/IMIX/Sign/DailySignInLineUpIMIX'
    data = {}
    response = requests.post(url, headers=headers, json=data)
    try:
        data = response.json()['data']['orderstatusdesc']
        if data == '排队签到中':
            print("签到成功")
    except:
        print("签到失败")
    headers = {
        "Host": "memberv5.imixpark.com",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "Authorization": "Bearer " + token,
        "buildingid": "80014",
        "xweb_xhr": "1",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541f0d) XWEB/25799",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx24d80b0b74d12b46/182/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url = 'https://memberv5.imixpark.com/fzapi/ApiScrmCusApp/IMIX/Sign/QueryBsActivitySignInfoIMIX'
    data = {}
    response = requests.post(url, headers=headers, json=data)

    score = response.json()['data']['memberinfo']['member_current_bonus']
    print("当前积分："+str(score))
def get_token(code):
    now = datetime.now()
    app_time = str(now).replace('-', '').replace(' ', '').replace(':', '').split('.')[0]
    txt = 'app_id=api.app.member&app_secret=AE859F714A309237&app_time='+app_time+'&appid=0af4654470625f46bd07b9a2c432b975&jscode='+code+'&roles=member&source=wx'
    app_sign = hex_md5(txt)
    headers = {
        'Host': 'memberv5.imixpark.com',
        'app_sign': app_sign.upper(),
        'app_time': app_time,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541f0d) XWEB/25715',
        'xweb_xhr': '1',
        'app_id': 'api.app.member',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://servicewechat.com/wx24d80b0b74d12b46/182/page-frame.html',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    json_data = {
	"source": "wx",
    "roles": "member",
	"appid": appid,
	"jscode": code
}
    response = requests.post('https://memberv5.imixpark.com/fzapi/ApiScrmApp/Token/Login', headers=headers,
                             json=json_data)
    access_token = response.json()['data']['access_token']
    print("获取token成功："+access_token)
    return access_token
def getcode(YYB_GO_URL,openid):
    url = f"{YYB_GO_URL}/wxapp/getCode"
    params = {"app_id": APPID,"ref": openid}
    # print(url,params)
    try:
        resp = requests.post(url=url, json=params, headers={"Content-Type": "application/json"})
        data = resp.json()
        code = data.get("data", {}).get("result",{}).get('code')
        print('获取code成功:'+code)
    except:
        print("获取code错误")
    return code

def mian():
    for i in YYB_SERVER.split():
        YYB_GO_URL = i.split("@")[0]
        openid = i.split("@")[1]
        code = getcode(YYB_GO_URL,openid)
        token = get_token(code)
        sign(token)
        get_score(token)

if __name__ == '__main__':
    try:
        mian()
    except:
        print("当前账号错误")


