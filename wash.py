import pandas as pd
import time
import numpy as np

t1=time.time()
path = r"allclass.csv"
data = pd.read_csv(path, encoding='GBK',encoding_errors='ignore')
print(data)
# 遍历每一行
def scanrows(data0):
    for index, row in data0.iterrows():
        print(row)

# 查看csv规模
def showsize():
    print(data.shape)

# 对不重复的行构建新的表

def newtable(data0):
    newdata = data0.drop_duplicates(keep=False)
    newdata.to_csv('newdata_all.csv', index=False)
    print(newdata)
    return newdata


def ts(data0):
    # 让结果的每一行也包括date
    pivot = pd.pivot_table(data0,index='date',values=['passage_count','read_total','read_viral','read_average','tops_total'
                                ,'likes_total', 'forward_total', 'WCI']
                            ,aggfunc={'passage_count':np.sum,'read_total':np.sum,'read_viral':np.sum,'read_average':np.mean,
                                      'tops_total':np.sum,'likes_total':np.sum,'forward_total':np.sum,'WCI':np.mean})
    pivot.reset_index(inplace=True, allow_duplicates=True)

    #scanrows(pivot)
    pivot.to_csv('pivot.csv', index=False)

ts(newtable(data))

t2=time.time()

print(t2-t1)
date=data['date'].values.tolist()
