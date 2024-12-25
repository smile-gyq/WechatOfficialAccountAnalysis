
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
url = 'https://www.gsdata.cn/rank/ajax_wxrank?'
    #'https://www.gsdata.cn/custom/ajax_comrankdetails?'
cookie = 'visitor_type=old; 53uvid=1; onliner_zdfq72213613=0; 53gid2=16475292202003; 53revisit=1728915146969; _gsdataCL=WzAsIjEzNzM1MTgyNDkwIiwiMjAyNDEyMTcwMTE3MTciLCI2ZmY3MzAxNmU0Y2YwZDYwZmYyMWMxNzRlNGFhZjUzZiIsNDc0Nzc3Nzg0XQ%3D%3D; _gsdataOL=474777784%3B13735182490%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%226%22%3A%22%22%2C%227%22%3A%22%22%2C%228%22%3A%22%22%2C%229%22%3A%22%22%2C%2299%22%3A%2220241217%22%7D%3B87cd8a02497ea4fb98be6ce97de81bcf; _identity-frontend=1c59df5be8a43bc93ab2281636efa1ed2c7632a0c0db09dcdb27f03ff4506482a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A31%3A%22%5B%22746209917%22%2C%22test+key%22%2C604800%5D%22%3B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzZDA3YTExNDg3ZTAtMGQ5Y2Q5MjkzYTE1MzYtNGM2NTdiNTgtMTMyNzEwNC0xOTNkMDdhMTE0OTE2OGUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; 53gid0=16475292202003; 53gid1=16475292202003; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1733640958,1733727759,1734369424,1734500804; HMACCOUNT=0F4051BA61FE16E4; PHPSESSID=msote3a711io5fmjbqoojem0s2; visitor_type=old; 53kf_72213613_from_host=www.gsdata.cn; uuid_53kf_72213613=af9b0ef5cc1892e2bdb546d649e34e01; 53kf_72213613_land_page=https%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; _csrf-frontend=d8bc107a11899832ca3061b8a68394b34a749130e43334153bbe50f5fbd3a0f1a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%2210QEAfaQF7t-jymPMFvlFx6Nqbb8hlzY%22%3B%7D; 53uvid=1; onliner_zdfq72213613=0; 53kf_72213613_keyword=https%3A%2F%2Fwww.gsdata.cn%2Frank%2Fwxrank; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1734504417'
    #'visitor_type=old; 53uvid=1; onliner_zdfq72213613=0; 53gid2=16475292202003; 53revisit=1728915146969; _gsdataCL=WzAsIjEzNzM1MTgyNDkwIiwiMjAyNDEyMTcwMTE3MTciLCI2ZmY3MzAxNmU0Y2YwZDYwZmYyMWMxNzRlNGFhZjUzZiIsNDc0Nzc3Nzg0XQ%3D%3D; _gsdataOL=474777784%3B13735182490%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%226%22%3A%22%22%2C%227%22%3A%22%22%2C%228%22%3A%22%22%2C%229%22%3A%22%22%2C%2299%22%3A%2220241217%22%7D%3B87cd8a02497ea4fb98be6ce97de81bcf; _identity-frontend=1c59df5be8a43bc93ab2281636efa1ed2c7632a0c0db09dcdb27f03ff4506482a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A31%3A%22%5B%22746209917%22%2C%22test+key%22%2C604800%5D%22%3B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzZDA3YTExNDg3ZTAtMGQ5Y2Q5MjkzYTE1MzYtNGM2NTdiNTgtMTMyNzEwNC0xOTNkMDdhMTE0OTE2OGUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; 53gid0=16475292202003; 53gid1=16475292202003; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1733640958,1733727759,1734369424,1734500804; HMACCOUNT=0F4051BA61FE16E4; PHPSESSID=msote3a711io5fmjbqoojem0s2; visitor_type=old; 53kf_72213613_from_host=www.gsdata.cn; uuid_53kf_72213613=af9b0ef5cc1892e2bdb546d649e34e01; 53kf_72213613_land_page=https%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; _csrf-frontend=d8bc107a11899832ca3061b8a68394b34a749130e43334153bbe50f5fbd3a0f1a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%2210QEAfaQF7t-jymPMFvlFx6Nqbb8hlzY%22%3B%7D; 53uvid=1; onliner_zdfq72213613=0; 53kf_72213613_keyword=https%3A%2F%2Fwww.gsdata.cn%2Frank%2Fwxrank; acw_tc=0aef812717345026554993883e0044a7aa7a70d0d989179fec85193fd4cf03; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1734504417'

    #'visitor_type=old; 53gid2=16475292202003; 53revisit=1728915146969; acw_tc=0aef815617343694114074833e004cca5c56080840143a49a7b37f357140f5; visitor_type=old; 53gid0=16475292202003; 53gid1=16475292202003; 53kf_72213613_from_host=www.gsdata.cn; uuid_53kf_72213613=746e2d9148289752fa22531099f3893e; 53kf_72213613_land_page=https%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; 53uvid=1; onliner_zdfq72213613=0; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1732959969,1733640958,1733727759,1734369424; HMACCOUNT=0F4051BA61FE16E4; _gsdataCL=WzAsIjEzNzM1MTgyNDkwIiwiMjAyNDEyMTcwMTE3MTciLCI2ZmY3MzAxNmU0Y2YwZDYwZmYyMWMxNzRlNGFhZjUzZiIsNDc0Nzc3Nzg0XQ%3D%3D; _gsdataOL=474777784%3B13735182490%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%226%22%3A%22%22%2C%227%22%3A%22%22%2C%228%22%3A%22%22%2C%229%22%3A%22%22%2C%2299%22%3A%2220241217%22%7D%3B87cd8a02497ea4fb98be6ce97de81bcf; 53kf_72213613_keyword=https%3A%2F%2Fu1.gsdata.cn%2F; _identity-frontend=1c59df5be8a43bc93ab2281636efa1ed2c7632a0c0db09dcdb27f03ff4506482a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A31%3A%22%5B%22746209917%22%2C%22test+key%22%2C604800%5D%22%3B%7D; PHPSESSID=f0g5t8i6tsu0rve6kmklbgjv36; _csrf-frontend=81f064a2be584e74afe5cd928ffe190216a0dda110d977ca52b8f670b634888ea%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22d1QChB8cyZTy83vl1G4CERvE10mQpvJH%22%3B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221928b5f7ed6ba7-0a2b796ee5f188-4c657b58-1327104-1928b5f7ed7864%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzZDA3YTExNDg3ZTAtMGQ5Y2Q5MjkzYTE1MzYtNGM2NTdiNTgtMTMyNzEwNC0xOTNkMDdhMTE0OTE2OGUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1734369503'

#### 使用Cookie，跳过登陆操作
# type是时间范围，每日数据就是“day”,周是"week"
# post_time的格式是“2024-12-05”，周是20241208_20241214
# page的格式是“2”
# "classify_type"是大类，没有就是“全部”
# "sontype"是细分类，没有就是""
# 省市区没有就是""

def get_1page(date,page1,classify_type1='',sontype1="",province1='',city1='',district1='',timefield='day'):
    data = {
        'type': timefield,
        'post_time': date,
        'page': page1,
        'classify_type': classify_type1,
        'son_type': sontype1,
        'province': province1,
        'city': city1,
        'district':district1,
        'types': 'undefined'
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

    for item, val in content_json1.items():
        if item != 'content_noencode':
            print(item, ":", val)
    return content_json1


#从一页排行榜中匹配出每一个公众号的所有数据
def re_findall(content,date1,timefield='day',classify_type1='',sontype1="",province1='',city1='',district1=''):
    specific_data_page=[]

    datamix = content["data"]
    #print(datamix)

    rank = re.findall(r'<span class="after-ten">(.*)</span>', datamix)
    rank123=re.findall(r'<span class="num-span no\d">(.*)</span>', datamix)

    #print(rank123)
    if len(rank)==0:
        rank = re.findall(r'<span class="num-span">(.*)</span>', datamix)
    if len(rank)==0:
        rank = rank123
    if rank[0]=='4' :
        rank=['1','2','3']+rank
    #print(rank)

    avatar = re.findall(r"src='(.*)'", datamix)
    #print(avatar)
    name = re.findall(r"<h1>(.*)</h1>", datamix)
    #print(name)
    title_id = re.findall(r"<span class=\"\">(.*)</span>", datamix)
    #print(title_id)
    passage_count = re.findall(r"<td><!-- / -->(.*)</td>", datamix)
    # print(passage_count)
    passage_data = re.findall(r"<td>(\d+(W\+)?)</td>|<td>(\d+\.\d+?)</td>", datamix)
    passage_data = [item[0] for item in passage_data]

    i=0
    for item in passage_data:
        if item=='':
            passage_data[i]='--'
        i += 1

    #print("passage_data:", passage_data)
    # print(len(passage_data))
    wci_thin = re.findall(r"<td>(\d+\.\d+?)</td>", datamix)

    wci=['0' for i in range(25)]
    if wci_thin != []:
        for i in range(len(wci_thin)):
            wci[i]=wci_thin[i]
    #print('a',wci)

    #print(wci)

    # 把上面匹配到的数据封装成一行一行的
    for i in range(len(rank)):
        specific_data_row = [timefield,date1,classify_type1,sontype1,province1,city1,district1]
        specific_data_row.append(rank[i])
        specific_data_row.append(name[i])
        specific_data_row.append(title_id[i])
        specific_data_row.append(passage_count[i])
        #正好这一page只有一行的时候，就要先判断有没有6个以上数据，有才能判断第7位是不是'--'
        if len(passage_data)>=7:
            if passage_data[6]=='--':
                specific_data_row.extend(passage_data[i * 7:i * 7 + 6])
            else:
                specific_data_row.extend(passage_data[i*6:i*6+6])
        else:
            specific_data_row.extend(passage_data[i * 6:i * 6 + 6])
        specific_data_row.append(wci[i])

        #print(specific_data_row)

        if avatar[i][:4]=='http':
            specific_data_row.append(avatar[i])
        else:
            specific_data_row.append('illegal-urlT-T')

        #一行写完之后，把每一行聚合到一起，最终是这一页
        specific_data_page.append(specific_data_row)

    #print(specific_data_page)
    return  specific_data_page


def get_a_day(date1,paramt1):
    day_data=[]
    date=date1
    paramt=paramt1
    for page in range(1,5):
        page1=str(page)
        #print(page1)
        a=get_1page(date,page1,classify_type1=paramt[0],sontype1=paramt[1],province1=paramt[2],city1=paramt[3],district1=paramt[4],timefield=paramt[5])
        #print(a)
        flag=1
        try:
            c=a['data']
        except:
            flag=0
            #print('----------')
        if flag==0:
            break
        b=re_findall(a,date,timefield=paramt[5],classify_type1=paramt[0],sontype1=paramt[1],province1=paramt[2],city1=paramt[3],district1=paramt[4])
        day_data.extend(b)
        #for item in b:
            #print(item)
        #print(b[0])
    return day_data


def get_a_month(paramt_in1):
    paramt_in = paramt_in1

    #以年为单位保存csv
    filename='daily-2024-'
    for item in paramt_in[:5]:
        if item=='':
            filename+='O'
        else:
            filename+=item
    filename+='.csv'

    #遍历月
    for month in month_list:
        month_data=[]
        days_start=1
        if month in ['5','7','8','10']:
            days_end=31
        elif month =='12':
            days_end=17
        else:
            days_end=30

        days_lenth = days_end - days_start
        days_list = []
        days_now = days_start

        #生成日期字段的列表，用于填充到header中
        for i in range(days_lenth+1):
            # 如果日期是个位数，要添一个0
            if days_now < 10:
                days_list.append(year+'-'+month+'-0'+str(days_now))
            else:
                days_list.append(year + '-' + month + '-' + str(days_now))
            days_now+=1
            #print(days_now)

        #遍历这个月的每一天
        for i in days_list:
            oneday=get_a_day(i,paramt_in)
            #把这一天的数据合并到这个月里
            month_data.extend(oneday)
            print(i,'已计入',len(oneday),end=' | ')
            if i[-1:]=='0':
                print('\n',end='')

        #写入这一月的数据
        name = ['timefield', 'date','class', 'subclass','province','city','district','rank','name','id',
                'passage_count','read_total', 'read_viral', 'read_average', 'tops_total',
                    'likes_total', 'forward_total', 'WCI','avatar']

        test = pd.DataFrame(columns=name, data=month_data)

        test.to_csv(filename, mode='a', encoding='GB18030')
        print('\n2024年', month, '月已存:',paramt_in)



# 按一级领域遍历
def classly_get():
    for class_now in class_list[1:2]:
        paramt_now=[class_now, '', '', '', '', 'day']
        get_a_month(paramt_now)

# 按省份遍历
def provincely_get():

    # 因为省份太多了，在本实验中减轻爬取时间成本，就爬取月榜数据
    filename='34provincely_12class1_6month.csv'
    # 生成date list
    date_list_month=['2024-06-01_2024-06-30','2024-07-01_2024-07-31','2024-08-01_2024-08-31','2024-09-01_2024-09-30',
                     '2024-10-01_2024-10-31','2024-11-01_2024-11-30']
    for province_now in province_list[1:]:
        #paramt_now=['全部', '', province_now, '', '', 'month']
        monthly_data =[]
        for class_now in class_list:
            paramt_now = [class_now, '', province_now, '', '', 'month']
            # 按月遍历
            for month_now in date_list_month:
                try:
                    monthly_data_row=get_a_day(month_now,paramt_now)
                except (requests.exceptions.JSONDecodeError,requests.exceptions.ConnectionError):
                    monthly_data_row=['err' for i in range(19)]
                #print(monthly_data_row)
                monthly_data.extend(monthly_data_row)
                print(province_now,class_now,month_now[:7],'已获取',end='|')
            print('\n',end='')
        # 一次性写入这一省份在这每个月的各领域的数据
        name = ['timefield', 'date', 'class', 'subclass', 'province', 'city', 'district', 'rank', 'name', 'id',
                'passage_count', 'read_total', 'read_viral', 'read_average', 'tops_total',
                'likes_total', 'forward_total', 'WCI', 'avatar']

        test = pd.DataFrame(columns=name, data=monthly_data)

        test.to_csv(filename, mode='a', encoding='GB18030')
        print(province_now,class_list, '已存:', )


###################################
#执行部分
t1=time.time()
year="2024"
month_list=['5','6','7','8','9','10','11','12']
#month_list=['8']
class_list=['财经','科技','文化','体育','娱乐','房产','教育','组织','旅游','健康','生活','其他']
subclass_list=[]
province_list=['河北省','山西省','辽宁省','吉林省','黑龙江省','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省',
'湖北省','湖南省','广东省','海南省','四川省','贵州省','云南省','陕西省','甘肃省','青海省','内蒙古自治区','广西壮族自治区','西藏自治区',
               '宁夏回族自治区','新疆维吾尔自治区','北京市','天津市','上海市','重庆市','台湾省','香港特别行政区','澳门特别行政区']
city_list=[]

# 执行部分
provincely_get()
#classly_get()

t2=time.time()
print(t2-t1)