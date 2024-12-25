import glob

csv_list=glob.glob('D:\Desktop\学校\大三上\领域大数据应用\期末大作业\清博日榜爬取\各领域日榜\*.csv')
print(csv_list)

for i in csv_list:
    fr=open(i,"r").read()
    with open("allclass_china_daily.csv",'a') as f:
        f.write(fr)
        f.close()

print('数据文件合并完成！')