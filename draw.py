import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts
import pandas as pd

class_list=['财经','科技','文化','体育','娱乐','房产','教育','组织','旅游','健康','生活','其他']

path = r"allclass_china_daily - 副本.csv"
data = pd.read_csv(path, encoding='GBK',encoding_errors='ignore')

date=data['date'].astype("str").values.tolist()

c1=data['top10readtotal_per'].values.tolist()
c2=data['top10read_per'].values.tolist()
c3=data['top10tops_per'].values.tolist()
c4=data['top10likes_per'].values.tolist()
c5=data['top10wci_per'].values.tolist()

'''
c=data['WCI'].values.tolist()
c1=data['财经'].values.tolist()
c2=data['科技'].values.tolist()
c3=data['文化'].values.tolist()
c4=data['体育'].values.tolist()
c5=data['娱乐'].values.tolist()
c6=data['房产'].values.tolist()
c7=data['教育'].values.tolist()
c8=data['组织'].values.tolist()
c9=data['旅游'].values.tolist()
c10=data['健康'].values.tolist()
c11=data['生活'].values.tolist()
c12=data['其他'].values.tolist()
'''


line = (Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=date)
    .add_yaxis(series_name="总阅读",y_axis=c1,is_symbol_show=False,is_smooth=True)
    .add_yaxis(series_name="篇均阅读",y_axis=c2,is_symbol_show=False,is_smooth=True)
    .add_yaxis(series_name="在看",y_axis=c3,is_symbol_show=False,is_smooth=True)
    .add_yaxis(series_name="点赞",y_axis=c4,is_symbol_show=False,is_smooth=True)
    .add_yaxis(series_name="平均WCI",y_axis=c5,is_symbol_show=False,is_smooth=True)
    )
line.render("头部数据占比趋势.html")