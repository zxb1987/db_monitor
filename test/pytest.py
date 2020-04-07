#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
#import xlrd
from pandas import Series,DataFrame


import pandas as pd
import numpy as np

orders = pd.read_excel("D:/info.xlsx")
#orders.groupby(['填报人','金额']).sum()

groups=orders.groupby(['填报人'])

print(orders['填报人'])

s=groups['金额'].sum()
c=groups['金额'].sum()

pt2=pd.DataFrame({'金额':s,'总金额':c})

# 定义ID为索引

# 生成excel文件output.xlsx，并保存到对应的位置。注意如果直接放到C盘可能会有问题！
pt2.to_excel('D:/按人员费用分类.xlsx')

