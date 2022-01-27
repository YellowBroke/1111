import requests
import json
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        start()
        print("退出线程：" + self.name)


cookie = "mcos.mpws=s%3AZIW3r2huQl5YyXFMHBszHwaD66mhq_3r.fvKgphpOQ%2BzGMes5bdbN5uVOaobtyIwMax%2FhM1b63VU"
tk = "e03ccfd1-dfcb-43b9-b7e4-a6137a265240"
date = "2021-12-10"
headers = {
    'Cookie': cookie,
    'tk': tk,
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030532)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate, br'
}


def start():
    data3 = json.dumps(
        {"date": date, "beginTime": "08:00", "endTime": "11:00",
         "deptId": "75", "staffId": "1010", "payMode": 1, "payCnl": "WX", "pid": 335022, "instId": "7"})
    while True:
        response3 = requests.post("https://mp.huameitai.com/anns/order/reg/reg", data=data3, headers=headers)
        time.sleep(1)
        print(response3.text)


# while int(time.time()) < 1638928500:
#     print("9:55开始运行，当前时间" + time.asctime(time.localtime(time.time())))
#     time.sleep(180)

for i in range(6):
    thread0 = myThread(i, str(i), i)
    thread0.start()


