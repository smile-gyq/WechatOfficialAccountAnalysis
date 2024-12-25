
# -*- coding: UTF-8 -*-
import requests
import time
import pandas as pd
import math
import random
import re

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
url = "https://www.gsdata.cn/rank/ajax_wxrank?type=day&post_time=2024-12-05&page=1&types=undefined&industry=all&proName=&industry_full=all&proName_full=&classify_type=%E5%85%A8%E9%83%A8&son_type=&province=&city=&district=&dataType=json"
cookie = "visitor_type=old; 53gid2=16475292202003; 53revisit=1728915146969; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%7D; _gsdataCL=WzAsIjEzNzM1MTgyNDkwIiwiMjAyNDEyMDgxNDU2MjQiLCJiZDY2M2Y3OWJmMzFlNGU3YzMwMDExMDE5ZDEzMDEzOCIsNDc0Nzc3Nzg0XQ%3D%3D; _gsdataOL=474777784%3B13735182490%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%226%22%3A%22%22%2C%227%22%3A%22%22%2C%228%22%3A%22%22%2C%229%22%3A%22%22%2C%2299%22%3A%2220241208%22%7D%3B66c1b043b28ccfff8153a2c25702179f; _identity-frontend=1c59df5be8a43bc93ab2281636efa1ed2c7632a0c0db09dcdb27f03ff4506482a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A31%3A%22%5B%22746209917%22%2C%22test+key%22%2C604800%5D%22%3B%7D; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1732280499,1732959969,1733640958,1733727759; HMACCOUNT=0F4051BA61FE16E4; visitor_type=old; 53kf_72213613_from_host=www.gsdata.cn; uuid_53kf_72213613=c16176b6af2663d3fc80ef4224e28f88; 53kf_72213613_land_page=https%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; 53uvid=1; onliner_zdfq72213613=0; _csrf-frontend=8fbe5993477b6938c836238da3e154725780664cf5a826a1f59b40fe2fe128ffa%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22gOCEIyG9dSsHLtxH3x09Nu5wZqr3579y%22%3B%7D; 53kf_72213613_keyword=https%3A%2F%2Fwww.gsdata.cn%2F; PHPSESSID=6eq3e4apuqrqkemo1ktluk5g55; 53gid1=16475292202003; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1733844849; acw_tc=1a0c380717338470852662526e0098f50397c70c0392acd5faf682fe13d5a1"

#### 使用Cookie，跳过登陆操作
# type是时间范围，每日数据就是“day”
# post_time的格式是“2024-12-05”
# page的格式是“2”
# "classify_type"是大类，没有就是“全部”
# "sontype"是细分类，没有就是""
def get_1page(date,page1,classify_type1='全部',sontype1="",timefield='day'):
    data = {
        "type": timefield,
        "post_time": date,
        "page": page1,
        "types": "undefined",
        "industry": "all",
        "industry_full": "all",
        "classify_type": classify_type1,
        "sontype":sontype1,
        "dataType": "json"
    }

    headers = {
        "host":"www.gsdata.cn",
        "referer":"https://www.gsdata.cn/rank/wxrank",
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"Windows",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "x-requested-with":"XMLHttpRequest",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Mobile Safari/537.36"
        }

    content_json1 = requests.get(url,headers=headers,params=data).json()
    print(content_json1)
    return content_json1


def re_findall(content,date,classify_type1='全部',sontype1="无",timefield='day'):
    datamix = content["data"]
    #print(datamix)

    rank = re.findall(r'<span class="num-span">(.*)</span>', datamix)
    print(rank)

    if len(rank)==22:
        rank=['1','2','3']+rank

    avatar = re.findall(r"src='(.*)'", datamix)
    #print(avatar)

    title = re.findall(r"<h1>(.*)</h1>", datamix)
    #print(title)

    title_id = re.findall(r"<span class=\"\">(.*)</span>", datamix)
    #print(title_id)

    passage_count = re.findall(r"<td><!-- / -->(.*)</td>", datamix)
    #print(passage_count)

    passage_data = re.findall(r"<td>(\d+(W\+)?)</td>|<td>(\d+\.\d+?)</td>", datamix)
    passage_data = [item[0] for item in passage_data]
    print("passage_data:",passage_data)
    #print(len(passage_data))

    wci = re.findall(r"<td>(\d+\.\d+?)</td>", datamix)
    #print(wci)

    passage_data_cut=[[],[],[],[],[],[]]

    for i in range(len(passage_data)):
        j = i % 7
        if j <= 5:
            passage_data_cut[j].append(passage_data[i])

    #for i in range(6):
        #print(passage_data_cut[i])
        #print(len(passage_data_cut[i]))

    print(rank)
    # 把上面提取出来的各个字段封装到content_list里
    content_list0=[]
    for i in range(25):
        items=[]
        #print(i)
        items.append(date)
        items.append(classify_type1)
        items.append(sontype1)
        items.append(timefield)
        items.append(rank[i])
        items.append(title[i])
        items.append(title_id[i])
        items.append(passage_count[i])
        items.append(passage_data_cut[0][i])
        items.append(passage_data_cut[1][i])
        items.append(passage_data_cut[2][i])
        items.append(passage_data_cut[3][i])
        items.append(passage_data_cut[4][i])
        items.append(passage_data_cut[5][i])
        items.append(wci[i])
        items.append(avatar[i])
        content_list0.append(items)

    print(content_list0[0])
    return content_list0


#执行部分

t1=time.time()
# 按每天爬取每一页,不能跨月份
year="2024"
month="11"
days_start=1
days_end=30
days_lenth=days_end-days_start

days_list=[]
days_now=days_start
for i in range(days_lenth+1):
    # 如果日期是个位数，要添一个0
    if days_now < 10:
        days_list.append(year+'-'+month+'-0'+str(days_now))
    else:
        days_list.append(year + '-' + month + '-' + str(days_now))
    days_now+=1
    print(days_now)

print(days_list)
content_list=[]

for i in days_list:
    print(i)
    for j in range(1,5):
        print(j)
        content_json=get_1page(i,j,classify_type1='全部',sontype1="",timefield='day')
        content_list.extend(re_findall(content=content_json,date=i,classify_type1='全部',sontype1="",timefield='day'))
        time.sleep(random.randint(4,9))
    time.sleep(random.randint(8,18))
name = ['date','classify_type1','sontype1','timefield','rank','title','title_id','passage_count','read_total','read_viral','read_average','tops_total','likes_total','forward_total','WCI','avatar']
#print(content_list)
test = pd.DataFrame(columns=name, data=content_list)
test.to_csv("202407gzh_top100_all_all.csv", mode='a', encoding='GB18030')
print("最后一次保存成功")

t2=time.time()
print('程序运行时间：',t2-t1)
a=input("ok:")