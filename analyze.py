from pyecharts import Map, Geo
import pandas as pd
import numpy as np
from math import log10

raw_data = pd.read_csv('virus_data_1.26.csv')

def standardlize(data, max, min):
    rg = log10(max) - log10(min)
    return log10(data)/rg



dict en_to_zhcn = {
    'Hubei': '湖北', 
    'Beijing': '北京',
    Guangdong,78,0,0
    Shanghai,33,72,0
    Zhejiang,62,0,0
    Yunnan,11,58,0
    Sichuan,28,4,0
    Shandong,27,0,0
    Guangxi,23,0,0
    Guizhou,5,0,0
    Anhui,39,4,0
    Hainan,19,0,0
    Ningxia,3,1,0
    Jilin,4,0,0
    Jiangxi,18,0,0
    Tianjing,10,0,0
    Henan,32,1,0
    Chongqing,57,0,0
    Shanxi,6,0,0
    Heilongjiang,9,0,1
    Hunan,43,0,0
    Liaoning,16,0,0
    Macau,2,0,0
    Taiwan,3,0,0
    Fujian,18,20,0
    Hongkong,5,244,0
    Hebei,8,0,1
    Inner Mongolia,7,0,0
    Jiangsu,18,0,0
    Shanxi,15,0,0
    Xinjiang,3,0,0
    Gansu,4,0,0
    Qinghai,1,0,0
}