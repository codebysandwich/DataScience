#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Photochemistry.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-05-24 08:38:30
# Last Modified Date: 2021-05-26 09:34:24
# Last Modified By  : sanwich <122079260@qq.com>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

plt.rcParams['font.family'] = ['Arial Unicode MS']


def twin_plot(data,
              axes,
              colors,
              labels,
              markers,
              ms=3.,
              l_fac=0.6,
              r_fac=0.85):
    """
    data: 待绘制数据，按列与颜色、y标签、图例标签对应 [shape: nx2]
    axes: 绘图区域
    colors: 绘图颜色
    labels: y轴标签
    ls: 线型样式
    markers: 点标记样式
    l_fac: 主轴压缩比例
    r_fac: 共享轴压缩比例
    """
    idx = list(range(len(data)))
    twin = axes.twinx()
    line1 = data.iloc[:, 0].to_numpy()
    line2 = data.iloc[:, 1].to_numpy()
    l1, = axes.plot(idx, line1, c=colors[0], marker=markers[0], ms=ms)
    l2, = twin.plot(idx, line2, c=colors[1], marker=markers[1], ms=ms)
    close_top_bottom_spines(axes)
    close_top_bottom_spines(twin)
    # ---------------colors--------------- #
    twin.spines['left'].set_color(l1.get_color())
    twin.spines['right'].set_color(l2.get_color())
    axes.tick_params(axis='y', color=l1.get_color(), labelcolor=l1.get_color())
    twin.tick_params(axis='y', color=l2.get_color(), labelcolor=l2.get_color())
    axes.set_ylabel(labels[0], color=l1.get_color())
    twin.set_ylabel(labels[1], color=l2.get_color())
    # ------------------------------ #
    axes.set_xlim(idx[0], idx[-1])
    axes.set_xticks([])
    axes.set_ylim(np.floor(np.nanmin(line1)),
                  np.ceil(np.nanmax(line1) / l_fac))
    twin.set_ylim(np.floor(np.nanmin(line2)),
                  np.ceil(np.nanmax(line2) / r_fac))
    twin.set_ylim()
    return l1, l2, twin


def vocs_plot(data, axes):
    # ---------------vocs绘制--------------- #
    length = len(data)
    idx = list(range(length))
    vocs = ['烷烃', '烯烃', '炔烃', '芳香烃', '卤代烃', 'OVOCs', '有机硫'][::-1]
    vocs_colors = [
        '#1600FF', '#00FF00', '#BFEAFF', '#FF0000', '#FFAA02', '#FF00CC',
        '#000000'
    ][::-1]
    # 绘制有机物堆叠图
    plots = axes.stackplot(idx,
                           data.loc[:, vocs].T,
                           colors=vocs_colors,
                           labels=vocs)
    axes.set_xlim(idx[0], idx[-1])
    ymin = data.loc[:, vocs].sum(axis=1).min()
    ymax = data.loc[:, vocs].sum(axis=1).max()
    axes.set_ylim(ymin, int(ymax / 0.7))
    handles, labels = axes.get_legend_handles_labels()
    axes.spines['top'].set_visible(False)
    axes.set_ylabel('VOCs(ppbv)')
    axes.legend(handles=reversed(handles),
                labels=reversed(labels),
                loc='upper center',
                ncol=len(vocs),
                edgecolor='w')
    ticks = [
        '{:d}:{:0>2d}\n{:d}/{:d}/{:d}'.format(dt.hour, dt.minute, dt.year,
                                              dt.month, dt.day)
        for dt in data.index.to_list()
    ]
    sli = axes.get_xticks()
    ticks = [ticks[int(i)] for i in sli if int(i) < length]
    axes.set_xticklabels(ticks)


def opts_plot(data, axes):
    # ---------------绘制光学参数--------------- #
    idx = list(range(len(data)))
    opts = ['PAN(μg/m³)', '紫外总辐射(W/m²)', 'JNO₂(#/s)']
    colors = ['k', '#AC73E6', '#FF80B3']
    ms = 3.
    twin_data = data[[opts[0], opts[-1]]]
    l1, l3, twin1 = twin_plot(twin_data,
                              axes,
                              colors=[colors[0], colors[-1]],
                              labels=[opts[0], opts[-1]],
                              markers=['^', 's'])
    line2 = data[opts[1]].to_numpy()
    twin2 = axes.twinx()
    twin2.spines['right'].set_position(("axes", 1.05))

    l2, = twin2.plot(idx, line2, c=colors[1], marker='d', ms=ms)
    close_top_bottom_spines(twin2)
    twin2.set_ylim(np.floor(np.nanmin(line2)),
                   np.ceil(np.nanmax(line2) / 0.85))
    # ---------------set color--------------- #
    twin2.spines['right'].set_color(l2.get_color())
    twin2.tick_params(axis='y',
                      labelcolor=l2.get_color(),
                      color=l2.get_color())
    twin2.set_ylabel(opts[1], color=l2.get_color())
    axes.legend(handles=[l1, l2, l3],
                labels=['PAN', '紫外辐射', 'JNO2'],
                loc='upper center',
                ncol=3,
                edgecolor='w')


def no_o3_plot(data, axes):
    idx = list(range(len(data)))
    no_o3 = ['O₃(μg/m³)', 'NO(μg/m³)', 'NO₂(μg/m³)']
    colors = ['#FF0000', '#01AAFF', '#0F00CC']
    twin_data = data[[no_o3[0], no_o3[-1]]]
    l1, l3, twin = twin_plot(twin_data,
                             axes,
                             colors=[colors[0], colors[-1]],
                             labels=[no_o3[0], 'NO,NO₂(μg/m³)'],
                             markers=['o', 'D'])
    l2, = twin.plot(idx, data[no_o3[1]].to_numpy(), ls='--', c=colors[1])
    dt = data[[no_o3[1], no_o3[2]]].to_numpy()
    twin.set_ylim(np.floor(np.nanmin(dt)), np.ceil(np.nanmax(dt) / 0.85))
    axes.legend(handles=[l1, l2, l3],
                labels=['O3', 'NO', 'NO₂'],
                loc='upper center',
                ncol=3,
                edgecolor='w')


def wind_plot(data, axes, arg=1):
    sd = ['风速(m/s)', '风向(°)']
    idx = list(range(len(data)))
    ws = data[sd[0]].to_numpy() / 8
    wd = data[sd[1]].to_numpy() * 180 / (-np.pi) + 270
    theta = (wd - 180) / 180 * np.pi
    ws = ws / np.nanmax(ws) * arg
    y = np.array([0] * len(data))
    u = ws * np.sin(theta)
    v = ws * np.cos(theta)
    axes.plot(idx, y, c='k')
    axes.quiver(idx,
                y,
                u,
                v,
                angles='xy',
                width=.0021,
                scale_units='xy',
                scale=1)
    close_top_bottom_spines(axes)
    axes.set_yticks([])
    axes.spines['right'].set_visible(False)
    axes.set_xlim(idx[0], idx[-1])
    axes.set_ylim(-arg, arg)
    axes.set_xticks([])
    axes.set_ylabel('风速风向', rotation='horizontal', labelpad=22)


def tp_plot(data, axes):
    tp = ['温度(℃)', '湿度(%)']
    colors = ['#FFAA02', '#01FFFF']
    twin_data = data[tp]
    l1, l2, twin = twin_plot(twin_data, axes, colors, tp, markers=['x', 'o'])
    axes.legend(handles=[l1, l2],
                labels=['温度', '湿度'],
                loc='upper center',
                ncol=2,
                edgecolor='w')


def close_top_bottom_spines(axes):
    axes.spines['top'].set_visible(False)
    axes.spines['bottom'].set_visible(False)


def photo_chemis_plot(data):
    """
    data: 光化学模版数据
    """
    fig = plt.figure(figsize=(14, 10))
    fig.subplots_adjust(right=0.9)
    gs = GridSpec(17, 1, figure=fig)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1:5, 0])
    ax3 = fig.add_subplot(gs[5:9, 0])
    ax4 = fig.add_subplot(gs[9:13, 0])
    ax5 = fig.add_subplot(gs[13:, 0])
    wind_plot(data, ax1)
    tp_plot(data, ax2)
    no_o3_plot(data, ax3)
    opts_plot(data, ax4)
    vocs_plot(data, ax5)
    plt.show()


if __name__ == "__main__":
    filepath = r'../../data/模板-光化学.xlsx'
    df = pd.read_excel(filepath,
                       sheet_name='igor粘贴',
                       index_col=0,
                       parse_dates=[0])
    # 选择时间段
    mask = (df.index >= pd.to_datetime('2021-05-08 00:00:00')) & (
        df.index < pd.to_datetime('2021-05-10 00:00:00'))
    photo_chemis_plot(df.iloc[mask, :])
