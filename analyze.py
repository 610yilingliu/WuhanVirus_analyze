from pyecharts.charts import Map
from pyecharts import options as opts

import pandas as pd
import numpy as np
from math import log10

def standardlize(data, max, min):
    if data != 0:
        return log10(data)/log10(max-min)
    return 0

en_to_zhcn = {
    'Hubei': '湖北',
    'Beijing': '北京',
    'Guangdong': '广东',
    'Shanghai': '上海',
    'Zhejiang': '浙江',
    'Yunnan': '云南',
    'Sichuan': '四川',
    'Shandong': '山东',
    'Guangxi': '广西',
    'Guizhou': '贵州',
    'Anhui': '安徽',
    'Hainan': '海南',
    'Ningxia':'宁夏',
    'Jilin':'吉林',
    'Jiangxi':'江西',
    'Tianjin':'天津',
    'Henan':'河南',
    'Chongqing': '重庆',
    'Shanxi': '山西',
    'Heilongjiang': '黑龙江',
    'Hunan': '湖南',
    'Liaoning':'辽宁',
    'Macau':'澳门',
    'Taiwan':'台湾',
    'Fujian':'福建',
    'Hongkong':'香港',
    'Hebei': '河北',
    'Inner Mongolia': '内蒙古',
    'Jiangsu': '江苏',
    'Shaanxi': '陕西',
    'Xinjiang': '新疆',
    'Gansu': '甘肃',
    'Qinghai': '青海',
    'Tibet':'西藏',
}


virus_data = pd.read_csv('virus_data_1.26.csv')

# Translate to Chinese
virus_data['Region_zhcn'] = virus_data['Region']
for i in range(len(virus_data)):
    virus_data['Region_zhcn'].replace(en_to_zhcn, inplace = True)

name = list(virus_data['Region_zhcn'])
infected_data = list(virus_data['Infected'])
standardlized = []
for i in range(len(infected_data)):
    standardlized.append(standardlize(infected_data[i], max(infected_data), min(infected_data)))


mapping = [[name[i], standardlized[i]] for i in range(len(name))]


infected_map = Map()
infected_map.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
    )
infected_map.set_global_opts(
    title_opts=opts.TitleOpts(title="People infected from Wuhan Virus"),
    visualmap_opts=opts.VisualMapOpts(
        is_show = False,
        max_= max(standardlized),
        range_text=["max", "min"],
        range_size= 1
        ),
    legend_opts=opts.LegendOpts(is_show = False),
    )

infected_map.add(" ", mapping, maptype = "china")
infected_map.render_notebook()
infected_map.render('map.html')