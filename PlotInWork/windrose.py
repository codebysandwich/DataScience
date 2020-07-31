# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2020-03-17 21:00:50
@LastEditTime: 2020-03-17 21:00:50
@LastEditors: sandwich
@Description: In User Settings Edit
@FilePath: /DSCore/windrose.py
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MAX_WINE_SPEED = 56
METHOD = 'ffill'

class WindRose:
    def __init__(self, data: pd.DataFrame):
        '''
        初始化数据
        数据需求3列：第一列风向，第二列风速，第三列污染物
        '''
        self.data = data
    
    def __maker(self, s, sequence):
        for i, val in enumerate(sequence):
            if s <= sequence[i+1]:
                return val

    def __check_size(self):
        '''
        检查数据
        '''
        col = self.data.shape[-1]
        if col != 3:
            raise ValueError("数据尺寸异常,列数为%d, 需求为3" % col)
        try:
            self.data = self.data.astype(np.float)
            # self.data = pd.to_numeric(self.data, errors='coerce')
        except Exception as e:
            raise ValueError("数据只能为数值类型！")
        max_degree, max_speed = self.data.iloc[:, 0].max(), self.data.iloc[:, 1].max()
        if max_degree > 360 or max_speed > MAX_WINE_SPEED:
            raise ValueError("风速风向数据异常!")


    def __fill_na(self):
        '''
        处理数据中的空值，填充方法默认向前填充
        '''
        self.data = self.data.fillna(method=METHOD)
        # 上边缘数据缺失按0背景值处理
        self.data = self.data.fillna(0)

    def __make_grid(self, speed_grid, deg_grid) -> pd.DataFrame:
        '''
        栅格化数据
        '''
        self.data.iloc[:, 0] = np.radians(self.data.iloc[:, 0])
        v, d = self.data.iloc[:, 1], self.data.iloc[:, 0]
        # 生成栅格数据所需的风速、风向格点
        speed = np.linspace(v.min(), v.max(), endpoint=True, num=speed_grid)
        deg = np.linspace(0, 2*np.pi, endpoint=True, num=deg_grid)
        # 将数据处理成格点
        self.data.iloc[:, 0] = d.apply(self.__maker, sequence=deg)
        self.data.iloc[:, 1] = v.apply(self.__maker, sequence=speed)
        # 栅格化数据
        cols = list(self.data.columns)
        dt = pd.pivot_table(self.data, values=cols[-1], index=cols[-2], columns=cols[0])
        dt.fillna(0, inplace=True)
        dt[2*np.pi] = 0
        dt = dt.reindex(columns=deg, index=speed, fill_value=0)
        return dt

    def plot(self, speed_grid=16, deg_grid=32):
        '''
        绘制污染玫瑰图🌹
        '''
        self.__check_size()
        self.__fill_na()
        dt = self.__make_grid(speed_grid, deg_grid)
        theta, r = np.meshgrid(dt.columns, dt.index)
        ax = plt.subplot(projection='polar')
        ax.set_theta_zero_location("N")
        ax.set_theta_direction('clockwise')
        pos = ax.contourf(theta, r, dt.to_numpy(), cmap='jet')
        plt.colorbar(pos, ax=ax)
        plt.show()