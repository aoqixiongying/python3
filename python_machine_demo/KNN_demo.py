# coding=utf-8
"""
@file: KNN_demo.py
@author: magician
@date: 2018/11/14
"""
import numpy as np
import pandas as pd


if __name__ == '__main__':
    # 读取鸢尾花的数据集,header参数来指定标题行,默认为0,如果没有标题,使用None
    data = pd.read_csv(r'/home/magician/project/python3/python_machine_demo/data_set/iris.csv', header=0)
    print(data)

