import requests
import json

header = {
    'Accept': '*/*',
    'Cookie': '_ntes_nnid=5336da7f6330130c0f3b1f38e4661f0e,1632585319816; _ntes_nuid=5336da7f6330130c0f3b1f38e4661f0e; wyy_uid=8a6e09df-ddbd-4968-a889-517805c319eb; channel="tag=M_tg_145_64"; pageContentBiz=GONG_GONG; pageContentBizProduct=""; abH=-1179248111; abTest=1; mp_MA-91DF-2127272A00D5_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fsf.163.com%2Fhome%3Ftag%3DM_tg_145_64%22%2C%22updatedTime%22%3A%201638761203906%2C%22sessionStartTime%22%3A%201638761203903%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22d122fbc2d221b4eac1b45cbb3cc7e7cc6daf488b%22%2C%22persistedTime%22%3A%201638761203898%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201638761203906%7D%2C%22sessionUuid%22%3A%20%22a891365daeda6ddb1c95ab1da94ca5a692049e2f%22%7D; _ga=GA1.2.110115317.1638761204; _iuqxldmzr_=32; NMTID=00ORZZvIS2yRBpQhEgllYKK2nDiPgsAAAF9689ZVw; WEVNSM=1.0.0; WNMCID=vjspjj.1640338774847.01.0; WM_TID=ThJX4F6hMjdEVRVRVBN5s2mBeUpLw%2F%2FH; playliststatus=visible; NTES_P_UTID=bAAGXP9YwvhZIqvjCOMfJoPT0hh3GepY|1640835507; NTES_SESS=qjZK9GRBBwSaHfeeE_FKBtWRxvXDxQB5WAJAySzv0DbKtMe.tG1VzrOim1M2uy5h6VgRu8AE2.VpY26hGlmdKLr6TzrUX0dAcd3K975kQ8VupXoQdzehntiF7Wy59yXdcIQjw57rELfYUf4P1v9LMMqpPwKPahjzLVac9YjWO8T9iEkzWCYXf.1CdbIayMcRws02DFs_HMQlRNZaxnL4ayCLo; NTES_PASSPORT=yZYM1ffeJj55EnktL0m2yKx2bJVei6h3vYOFicyaQIUE490e4zw3CZ25dw9fPUsqy3tFPbEHfe3C7sVdXTzyK_9uAFMffIED40ql5yBVkofhOKhxBOAtQzH4Uaa.1Oxsduipkmod3RxExHmGUSlqnK5DIXHVzVpaaGrX_nesRhw1kNDnkg3Q9Ro_mA0wVPWK.; S_INFO=1640835507|0|3&80##|net_hybrid_music; P_INFO=net_hybrid_music@163.com|1640835507|1|mail163|00&99|gud&1640832989&unireg#gud&441200#10#0#0|&0|unireg|net_hybrid_music@163.com; nts_mail_user=net_hybrid_music@163.com:-1:1; MUSIC_EMAIL_U=36a74861e5c9a0c46a847807762a52e6fe9734fd454f15574e98ce52e946e36f44099f6db87894622a3d12e511a306e59c01b1245ca5469705925a4e6992f61de758fe0f42e016623058a731ea016156; csrfToken=7Q9rgtJqCGL8em8684qa4GBG; ntes_kaola_ad=1; JSESSIONID-WYYY=rIzOGwSEyri78u1vbZb883zWm%2BFcncd03%2FGG9Dp0mUNHRctoUsH7QQ4u%5CRWRfEvZePEXoU5dBZB2%5CRSzfBIAn%2BKgMZXt%2Fjk4hpMTHPq8E%5CRODkokC3gQjXtY%2F2qooYdghas3StUAHUwqwdhThgjTawn90G%2B6tFwq5l0QNiszgIbF0rW%2B%3A1641261594660; WM_NI=047p8lQ8p04q2CvKneCLBqix0Zc%2FjCHHZo5EkLjBH08T6UqjolhfiMADs7T8XQEgS6W4D0XRzQQoqC9%2Bk7gnMbUdJ9OdpJf2OvmiXnBCc%2BxxQX8%2BdfwXgTmmMe1khI0Wa3Y%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaae95cfb97f9abc673aebc8aa6c55b829a9babf53e87a9828eec50f5b2b9bbe42af0fea7c3b92af4ecf991bb6893e8c0d1b77bf29dbaaced6f81948e92ec74f486add0e9498c989690b84fa994a6a3cb3cfc8cfab6f462adb4a887ec47839cbdd8d7349c8f8b88d23e95ec8cd1db5aba8f9f90f449fbf5a5d8e6668fbe9b85c9338dbcc0abe53a8daaa38adb66829dadccfb749388f8cce76eb588a9b5f0678fbbff8ceb43f489afd4dc37e2a3; __snaker__id=UAq199cnHHQkUE7X; _9755xjdesxxd_=32; MUSIC_U=e98c194ce0df7b04e49439e4ebcc9ef0617a75c6e440e1d39b36512f8a5e6e684e628e97ad399181b4f3624270ad0c63ce2370418fd34f819c01b1245ca5469705925a4e6992f61de758fe0f42e016623058a731ea016156; __csrf=b282751ceeceb5541ad5fb67604c5891; __remember_me=true; gdxidpyhxdE=a8Lh%2BIIwK9DRkhHJ1pP%2BqL37TvZG5RfEvuJQ5wlZsZ%2BVUA%5CpxNqo2y89kRg4yBmJOtXsJws8lXSGmZGCum8VeILMQK3g10JY5TOUZeP1v12f53KKgHxoOtrQSg8wHpnCoCaVOpQ9vzL6vg5%2FMpAynMBEEXGHh%2F5G1Rwey4w9PYAOnXHo%3A1641261943054',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Dest': 'empty',
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': "Windows",
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/user/songs/rank?id=332486961',
}
# 获取歌单歌曲id
datas = {"id": 3778678, "n": 100000, "s": 8}
re = requests.post("https://music.163.com/api/v6/playlist/detail", datas, header)
jsonaaa = json.loads(re.text)
f = open("songlist.txt", 'a')
for song in jsonaaa["playlist"]["trackIds"]:
    f.write(str(song["id"]) + '\n')

set1 = set()

f = open("songlist.txt", 'r')
for songId in f.readlines():
    songId = songId.strip('\n')
    for i in range(50):
        offset = i * 20
        reesss = requests.get("https://music.163.com/api/v1/resource/comments/R_SO_4_" + str(songId) + "?limit=20&offset=" + str(offset))
        print(i)
        aaaa = json.loads(reesss.text)
        for comment in aaaa["comments"]:
            set1.add(comment["user"]["userId"])


f = open("userId.txt", 'a')
for elem in set1:
    f.write(str(elem) + '\n')
f.close()