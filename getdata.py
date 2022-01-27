import requests
from bs4 import BeautifulSoup
import os, json
import base64
from Crypto.Cipher import AES
from prettytable import PrettyTable
import warnings

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

warnings.filterwarnings("ignore")
BASE_URL = 'http://music.163.com/'
_session = requests.session()
COMMENT_COUNT_LET = 100000

url = "https://music.163.com/api/play-record/song/list"
header = {
    'Accept': '*/*',
    'Cookie': '_ntes_nnid=5336da7f6330130c0f3b1f38e4661f0e,1632585319816; _ntes_nuid=5336da7f6330130c0f3b1f38e4661f0e; wyy_uid=8a6e09df-ddbd-4968-a889-517805c319eb; channel="tag=M_tg_145_64"; pageContentBiz=GONG_GONG; pageContentBizProduct=""; abH=-1179248111; abTest=1; mp_MA-91DF-2127272A00D5_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fsf.163.com%2Fhome%3Ftag%3DM_tg_145_64%22%2C%22updatedTime%22%3A%201638761203906%2C%22sessionStartTime%22%3A%201638761203903%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22d122fbc2d221b4eac1b45cbb3cc7e7cc6daf488b%22%2C%22persistedTime%22%3A%201638761203898%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201638761203906%7D%2C%22sessionUuid%22%3A%20%22a891365daeda6ddb1c95ab1da94ca5a692049e2f%22%7D; _ga=GA1.2.110115317.1638761204; _iuqxldmzr_=32; NMTID=00ORZZvIS2yRBpQhEgllYKK2nDiPgsAAAF9689ZVw; WEVNSM=1.0.0; WNMCID=vjspjj.1640338774847.01.0; WM_TID=ThJX4F6hMjdEVRVRVBN5s2mBeUpLw%2F%2FH; playliststatus=visible; NTES_P_UTID=bAAGXP9YwvhZIqvjCOMfJoPT0hh3GepY|1640835507; NTES_SESS=qjZK9GRBBwSaHfeeE_FKBtWRxvXDxQB5WAJAySzv0DbKtMe.tG1VzrOim1M2uy5h6VgRu8AE2.VpY26hGlmdKLr6TzrUX0dAcd3K975kQ8VupXoQdzehntiF7Wy59yXdcIQjw57rELfYUf4P1v9LMMqpPwKPahjzLVac9YjWO8T9iEkzWCYXf.1CdbIayMcRws02DFs_HMQlRNZaxnL4ayCLo; NTES_PASSPORT=yZYM1ffeJj55EnktL0m2yKx2bJVei6h3vYOFicyaQIUE490e4zw3CZ25dw9fPUsqy3tFPbEHfe3C7sVdXTzyK_9uAFMffIED40ql5yBVkofhOKhxBOAtQzH4Uaa.1Oxsduipkmod3RxExHmGUSlqnK5DIXHVzVpaaGrX_nesRhw1kNDnkg3Q9Ro_mA0wVPWK.; S_INFO=1640835507|0|3&80##|net_hybrid_music; P_INFO=net_hybrid_music@163.com|1640835507|1|mail163|00&99|gud&1640832989&unireg#gud&441200#10#0#0|&0|unireg|net_hybrid_music@163.com; nts_mail_user=net_hybrid_music@163.com:-1:1; MUSIC_EMAIL_U=36a74861e5c9a0c46a847807762a52e6fe9734fd454f15574e98ce52e946e36f44099f6db87894622a3d12e511a306e59c01b1245ca5469705925a4e6992f61de758fe0f42e016623058a731ea016156; WM_NI=PJjzwBMFjMdPQkNdqPtSUxbf2gTS7Z0jeqrxtyDhfCX%2F6NpnF12KSpB7eUDfr%2BIDUSV9iKA1s%2BjjyMp6PLy22Ap%2F%2BYcwDFN8gyV%2BLdjZxVK%2F7Z1FlxGFPRp%2BK3qfAaO8M1Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3f04085e79eb2f643e9a88aa6d45e969a8abaae259396ffccaa40b28effd4c22af0fea7c3b92a9496a69bf64a8f9aa6aee75c93b58285f45cb88d9b99e16ef2b99cb4b652f4b6ab92f174b8a78c89e5499cf1faaff36686effeacd27c82e9abb6c76eb2f587a5d85996e7a7acc43bb1f5a68bfc47b4eaa0adfc3af29fc0d0aa53a1a98ca7cd34a5a79acccf70aa86b8b7ca25f586ffa7ef74859aa0b3f32189edbf87c46b8de883d2d437e2a3; csrfToken=7Q9rgtJqCGL8em8684qa4GBG; __csrf=639c1766da997ba2635d0f02d430ee0e; MUSIC_U=e98c194ce0df7b04e49439e4ebcc9ef0617a75c6e440e1d39b36512f8a5e6e684e628e97ad399181bb2985ee0d4c62dd0f946cbac193314b9c01b1245ca5469705925a4e6992f61de758fe0f42e016623058a731ea016156; __remember_me=true; ntes_kaola_ad=1; JSESSIONID-WYYY=KM5Qf0xZhAGVu%2FSr3VFowuAve7AW05FN72j04nOFEaDZf3%2F6%2F0hgJaJS8VWX3v9K33OumWoZ5egqkVb0ZxSS0cS%2B2HNXSF0s5XnDi5%2B98kGHW0A0%5COSS9ajC%2FyyN1Ont%2BdDTAlSl3IDzifOE6KuNnoIrUvdcEVKiR6%2FFD%2FpP24Wd59Mn%3A1641055961075',
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
    'referer': 'https://music.163.com/user/songs/rank?id=332486961'
}
