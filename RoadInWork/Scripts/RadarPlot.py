#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : RadarPlot.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-05-21 10:17:07
# Last Modified Date: 2021-05-21 15:57:52
# Last Modified By  : sanwich <122079260@qq.com>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
"""
数据空间分辨率单位为km
"""


def radar_pcolor(data,
                 blind=0.2,
                 show_height=5,
                 vmin=0,
                 vmax=1,
                 cmap='cas',
                 height_dpi=1,
                 show=True,
                 pic_path=None):
    """
    data: 列为廓线的dataframe数据，廓线高度单位为km
    blind: 盲区高度,单位km
    show_height: 数据显示有效区域，默认5km
    vmin: 绘图(伪彩色对应最高值)最小值，默认0
    vmax: 绘图(伪彩色对应最高值)默认1
    cmap: 伪彩图色彩样式，默认公司配色
    height_dpi: 高度刻度精度，单位km
    show: 调出图片显示窗口
    pic_path: 图片存储地址，默认不存储
    """
    # 获取数据长度及对应雷达数据最大高度
    H, height = len(data), data.index[len(data) - 1]
    fig, axes = plt.subplots(figsize=(12, 4))
    # 依据显示高度定位取值上限
    _sli = int(H / height * show_height)
    # 处理盲区
    _data = data.iloc[int(H / height * blind):_sli, :]

    if cmap == 'cas':
        colors = [
            '#2F59B9', '#00ADA8', '#00F200', '#E1F700', '#E99900', '#FF0012'
        ]
        cmap = LinearSegmentedColormap.from_list('mymap', colors)

    p = axes.imshow(_data,
                    vmax=vmax,
                    vmin=vmin,
                    origin="lower",
                    aspect='auto',
                    cmap=cmap)

    # 处理高度轴标签与刻度
    tic = H // height
    s_tic = np.round(
        np.arange(height_dpi, height_dpi + show_height, step=height_dpi), 1)
    s_tic = np.where(s_tic > show_height, show_height, s_tic)
    d_tic = (s_tic - blind) * tic
    d_tic = [0] + list(d_tic)
    s_tic = [blind] + list(s_tic)
    plt.yticks(d_tic, s_tic)

    idx = list(plt.xticks()[0][1:].astype(int))[:-1]
    plt.xticks(
        idx, [str(data.columns[item])[:-3].replace(' ', '\n') for item in idx])
    plt.colorbar(p)

    if pic_path:
        plt.savefig(pic_path)
    if show:
        plt.show()


if __name__ == "__main__":
    filepath = r'../../data/lidarData.txt'
    df = pd.read_csv(filepath, index_col=0).iloc[:, :-1]
    radar_pcolor(df, blind=0.3, show_height=5, cmap='cas', height_dpi=0.5)
