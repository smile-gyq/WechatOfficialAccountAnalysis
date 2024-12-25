
# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
import math
import random
#import 公众号正文爬取

t1=time.time()
global user_agent_list
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",
]

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
cookie = "appmsglist_action_3899850631=card; RK=RtFgyh7yS2; ptcz=9d0e2c79d110e5bb69977fc8133bc10722dc7bb3fe65ddf1b1d3549ebb152517; _qimei_uuid42=18717020c0b100b99c906abe99e9a65eb3443d375a; pac_uid=0_TRFRNiazj6eRZ; _qimei_q36=; _qimei_h38=fdee9f919c906abe99e9a65e02000006018717; pgv_pvid=1672209985459810; fqm_pvqid=6a505d60-bb47-453e-a1a1-bfaf13aa1bc6; ua_id=1nTjRw67luD0sc4dAAAAAMI0yOVK1UViP8Ukqy49z-A=; wxuin=24486911293517; mm_lang=zh_CN; _qimei_fingerprint=95f2638e6c4f46e8ca34e527b7df81c9; suid=user_0_TRFRNiazj6eRZ; personAgree_3899850631=true; fopenid=1EE7494FB9BAEB54A823CB591252459F; openid=1EE7494FB9BAEB54A823CB591252459F; token=32AF8AFBE68742682626CCA4F4C64D75; it_c=0; ts_uid=9152816520; pgv_pvi=3844520960; _qpsvr_localtk=0.6266649931297696; cert=CbJf1_bvdmpvz7CAxd55KRvpiPWcsbFY; _ga=GA1.1.1243785240.1733762128; pgv_info=ssid=s1717337624325166; _ga_0EKMG65RQ9=GS1.1.1733762127.1.1.1733762499.0.0.0; rewardsn=; wxtokenkey=777; _clck=3899850631|1|frn|0; uuid=6961c88d4828079ae10ccdbf736fe816; rand_info=CAESIGhfJCLYHU8a5Yyp7mQBZHw8iCh3XOXFSnOCdcG9pshy; slave_bizuin=3899850631; data_bizuin=3899850631; bizuin=3899850631; data_ticket=Tsi3xKbhbplInNn5VeWhy1EhQG+n+1l3opL6qvkitGlsRBA4CMZLHzEz/hcFpvBB; slave_sid=aFVaV1lzd0ZUT1ZybVJOT0EwMElvVGpheXNYVzkzc0Vta0lkSFpKS3NvUE92cnhHT09pTWVYQjhYeGVsMXpyNngxVTdEME5DRERZNHF2UHZuekJiV21tV1FEWEZCU2dHUHFnM1dPdEkzTXpBZkc2UEdJZEZGUElmSnFHdzUyYkZ3RzExbkhVYWdvdXBjZ2o0; slave_user=gh_096a616da4f8; xid=43d0b403f9c21b6c93bb9bf992b4c24a; _clsk=1idfbwj|1734019788011|10|1|mp.weixin.qq.com/weheat-agent/payload/record"

    #'RK=RtFgyh7yS2; ptcz=9d0e2c79d110e5bb69977fc8133bc10722dc7bb3fe65ddf1b1d3549ebb152517; _qimei_uuid42=18717020c0b100b99c906abe99e9a65eb3443d375a; pac_uid=0_TRFRNiazj6eRZ; _qimei_q36=; _qimei_h38=fdee9f919c906abe99e9a65e02000006018717; pgv_pvid=1672209985459810; fqm_pvqid=6a505d60-bb47-453e-a1a1-bfaf13aa1bc6; ua_id=1nTjRw67luD0sc4dAAAAAMI0yOVK1UViP8Ukqy49z-A=; wxuin=24486911293517; mm_lang=zh_CN; _qimei_fingerprint=95f2638e6c4f46e8ca34e527b7df81c9; suid=user_0_TRFRNiazj6eRZ; personAgree_3899850631=true; fopenid=1EE7494FB9BAEB54A823CB591252459F; openid=1EE7494FB9BAEB54A823CB591252459F; token=32AF8AFBE68742682626CCA4F4C64D75; it_c=0; ts_uid=9152816520; pgv_pvi=3844520960; _ga=GA1.1.1243785240.1733762128; _ga_0EKMG65RQ9=GS1.1.1733762127.1.1.1733762499.0.0.0; _clck=3899850631|1|frn|0; rand_info=CAESIGhfJCLYHU8a5Yyp7mQBZHw8iCh3XOXFSnOCdcG9pshy; slave_bizuin=3899850631; data_bizuin=3899850631; bizuin=3899850631; data_ticket=Tsi3xKbhbplInNn5VeWhy1EhQG+n+1l3opL6qvkitGlsRBA4CMZLHzEz/hcFpvBB; slave_sid=aFVaV1lzd0ZUT1ZybVJOT0EwMElvVGpheXNYVzkzc0Vta0lkSFpKS3NvUE92cnhHT09pTWVYQjhYeGVsMXpyNngxVTdEME5DRERZNHF2UHZuekJiV21tV1FEWEZCU2dHUHFnM1dPdEkzTXpBZkc2UEdJZEZGUElmSnFHdzUyYkZ3RzExbkhVYWdvdXBjZ2o0; slave_user=gh_096a616da4f8; xid=43d0b403f9c21b6c93bb9bf992b4c24a; poc_sid=HEobW2ejeQGzz3xKwNkWboFc0xewkRf3DtNTIZca; rewardsn=; wxtokenkey=777'

# 使用Cookie，跳过登陆操作
data = {
    "token": "357982587",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    #fakeid只有换公众号才用更新
    "fakeid": 'MzA5MjM3MzUxMA==',
        #"MjM5Njk3Nzg4Mg==",
    "type": "9",
}
headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",

    }

content_json = requests.get(url, headers=headers, params=data).json()
print(content_json)
count = int(content_json["app_msg_cnt"])
print(count)
page = int(math.ceil(count / 5))
print(page)
content_list = []
# 功能：爬取IP存入ip_list列表

full_content_list=[]
for i in range(441,821):
    data["begin"] = i * 5
    user_agent = random.choice(user_agent_list)
    headers = {
        "Cookie": cookie,
        "User-Agent": user_agent,
    }
    ip_headers = {
        'User-Agent': user_agent
    }
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()

    '''
    for item in content_json["app_msg_list"]:
        print(item)
    '''

    # 返回了一个json，里面是每一页的数据
    aaa=1
    for item in content_json["app_msg_list"]:
        if aaa==1:
            #print(item)
            aaa=0
        # 提取每页文章的标题及对应的url
        items = []
        items.append(item["title"])
        items.append(item["link"])
        t = time.localtime(item["create_time"])
        items.append(time.strftime("%Y-%m-%d %H:%M:%S", t))
        content_list.append(items)
        f=0

        ####调用爬取正文详细数据的方法，存到full里
        #full_content_list.append(get_content(item["link"]))

        '''
        if f == 0:
            print("---------------------------------------")
            print(content_list)
            f = 1
        '''

    #print(i)
    if (i > 0) and (i % 20 == 0):
        name = ['title', 'link', 'create_time']
        test = pd.DataFrame(columns=name, data=content_list)
        test.to_csv("url3-GB.csv", mode='a', encoding='GB18030')
        print(">>>第" + str(int(i/20+1)) + "次存表成功")
        content_list = []
        #每20页歇息一分多钟
        time.sleep(random.randint(15,45))
    else:
        #每1页歇息十几秒
        time.sleep(random.randint(5,10))
        print('第'+str(i+1)+'次保存成功')

name = ['title', 'link', 'create_time']
test = pd.DataFrame(columns=name, data=content_list)
test.to_csv("url3-GB.csv", mode='a', encoding='GB18030')

print("最后一次保存成功")

'''
name2 = ['nick_name','create_time','title','text','ip_wording','advertisement_info','cdn_url','outer_link_num','picture_info_list','link']
test2 = pd.DataFrame(columns=name2, data=full_content_list)
test2.to_csv("article_details.csv", mode='a', encoding='GB18030')
'''
t2=time.time()
print('用时:',t2-t1)