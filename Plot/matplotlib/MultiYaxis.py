#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : MultiYaxis.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-05-19 17:20:27
# Last Modified Date: 2021-05-20 16:55:42
# Last Modified By  : sanwich <122079260@qq.com>

import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)
    twin1 = ax.twinx()
    twin2 = ax.twinx()

    twin2.spines['right'].set_position(("axes", 1.2))

    p1, = ax.plot([0, 1, 2], [0, 1, 2], "b-", label="Density")
    p2, = twin1.plot([0, 1, 2], [0, 3, 2], "r-", label="Temperature")
    p3, = twin2.plot([0, 1, 2], [50, 30, 15], "g-", label="Velocity")

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    twin1.set_ylim(0, 4)
    twin2.set_ylim(1, 65)

    ax.set_xlabel("Distance")
    ax.set_ylabel("Density")
    twin1.set_ylabel("Temperature")
    twin2.set_ylabel("Velocity")

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p2.get_color())
    twin2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=6, width=1.5)
    ax.tick_params(axis='y',
                   color=p1.get_color(),
                   labelcolor=p1.get_color(),
                   **tkw)
    twin1.tick_params(axis='y',
                      color=p2.get_color(),
                      labelcolor=p2.get_color())
    twin2.tick_params(axis='y',
                      color=p3.get_color(),
                      labelcolor=p3.get_color())

    for axes in [ax, twin1, twin2]:
        axes.spines['top'].set_visible(False)
        axes.spines['bottom'].set_visible(False)

    ax.legend(handles=[p1, p2, p3])

    twin2.spines['left'].set_color('b')

    plt.show()
