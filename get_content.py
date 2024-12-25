
# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
import math
import random
import re

global user_agent_list

t1=time.time()
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

def get_an_article(url0):
    data_row=[]

    # 目标url
    url = url0
    cookie = 'RK=RtFgyh7yS2ptcz=9d0e2c79d110e5bb69977fc8133bc10722dc7bb3fe65ddf1b1d3549ebb152517_qimei_uuid42=18717020c0b100b99c906abe99e9a65eb3443d375apac_uid=0_TRFRNiazj6eRZ_qimei_q36=_qimei_h38=fdee9f919c906abe99e9a65e02000006018717pgv_pvid=1672209985459810fqm_pvqid=6a505d60-bb47-453e-a1a1-bfaf13aa1bc6ua_id=1nTjRw67luD0sc4dAAAAAMI0yOVK1UViP8Ukqy49z-A=wxuin=24486911293517mm_lang=zh_CN_qimei_fingerprint=95f2638e6c4f46e8ca34e527b7df81c9suid=user_0_TRFRNiazj6eRZpersonAgree_3899850631=truefopenid=1EE7494FB9BAEB54A823CB591252459Fopenid=1EE7494FB9BAEB54A823CB591252459Ftoken=32AF8AFBE68742682626CCA4F4C64D75it_c=0ts_uid=9152816520pgv_pvi=3844520960_ga=GA1.1.1243785240.1733762128_ga_0EKMG65RQ9=GS1.1.1733762127.1.1.1733762499.0.0.0_clck=3899850631|1|frn|0rand_info=CAESIGhfJCLYHU8a5Yyp7mQBZHw8iCh3XOXFSnOCdcG9pshyslave_bizuin=3899850631data_bizuin=3899850631bizuin=3899850631data_ticket=Tsi3xKbhbplInNn5VeWhy1EhQG+n+1l3opL6qvkitGlsRBA4CMZLHzEz/hcFpvBBslave_sid=aFVaV1lzd0ZUT1ZybVJOT0EwMElvVGpheXNYVzkzc0Vta0lkSFpKS3NvUE92cnhHT09pTWVYQjhYeGVsMXpyNngxVTdEME5DRERZNHF2UHZuekJiV21tV1FEWEZCU2dHUHFnM1dPdEkzTXpBZkc2UEdJZEZGUElmSnFHdzUyYkZ3RzExbkhVYWdvdXBjZ2o0slave_user=gh_096a616da4f8xid=43d0b403f9c21b6c93bb9bf992b4c24apoc_sid=HEobW2ejeQGzz3xKwNkWboFc0xewkRf3DtNTIZcarewardsn=wxtokenkey=777'

    data = {
        #'appmsgid': '2651392290',
        #"lang": "zh_CN",
        #'comment_id': '3765024866596667402',
        #'content_size': '881',
        'pc_version': '1',
        'shareline_time': '',
        'uin': '',
        'key': '',
        #'pass_ticket': '',
        'wxtoken': '777',
        'devicetype': '',
        'clientversion': 'false',
        'version': 'false',
        '__biz': 'MjM5Njk3Nzg4Mg==',
        'appmsg_token': '',
        'x5': '0',
        'f': 'json'
    }

    headers = {
            "Cookie": cookie,
            "User-Agent": random.choice(user_agent_list)
                #"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36",
        }
    try:
        content_json = requests.get(url, headers=headers, params=data).json()
        #print(content_json)

        data_row.append(content_json['nick_name'])
        data_row.append(content_json['create_time'])
        data_row.append(content_json['title'])

        '''
        print(content_json['nick_name'])
        print(content_json['title'])
        print(content_json['desc'])
        print(content_json['content_noencode'])
        print(len(content_json['content_noencode']))
        print('')
        '''
        '''
        for item,val in content_json.items():
            if item != 'content_noencode':
                print(item,":",val)
        '''
        print(content_json)
        text = re.findall('>(.*?)<', content_json['content_noencode'])
        #print(len(text))
        #print(text)
        for i in range(text.count('')):
            text.remove('')
        #print(text)
        #print(len(text))

        text_merge=''.join(text)

        data_row.append(text_merge)
        data_row.append(content_json['ip_wording'])
        data_row.append(content_json['advertisement_info'])
        data_row.append(content_json['cdn_url'])
        data_row.append(content_json['use_outer_link'])
        data_row.append(content_json['picture_page_info_list'])
        data_row.append(content_json['link'])

    except:
        print('!!!!!!!!!!!!!!!!',url0)
        r=[[] for i in range(10)]
        r[0]=url0
        return r

    return data_row



name = ['nick_name','create_time','title','text','ip_wording','advertisement_info','cdn_url','outer_link_num','picture_info_list','link']

path = r"url3-GB2.csv"
url_data = pd.read_csv(path, encoding='GBK',encoding_errors='ignore')
url_list = url_data['link'].values.tolist()
#print(len(url_list))
if 'link' in url_list:
    url_list.remove('link')
#print(len(url_list))  # 一维列表

content_list=[]
i=0
for link_now in url_list[825:1334]:
    #print(link_now)
    new_row = get_an_article(url0=link_now)
    if new_row[0] != 'link':
        content_list.append(new_row)
        i+=1
    print('第'+str(i)+'个链接爬取成功')
    time.sleep(random.randint(1,7))

test = pd.DataFrame(columns=name, data=content_list)
test.to_csv("article_details3.csv", mode='a', encoding='GB18030')

print("最后一次保存成功")

t2=time.time()
print('用时:',t2-t1)