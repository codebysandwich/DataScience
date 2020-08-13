<!--
 * @Author: sandwich
 * @Date: 2020-07-28 09:05:08
 * @LastEditTime: 2020-08-13 21:17:19
 * @LastEditors: sandwich
 * @Description: 工作绘图开源文档
 * @FilePath: /DataScience/PlotInWork/README.md
--> 
# 日常工作中的绘图-Python实现


![logo](https://i.loli.net/2020/07/28/X5WEUHuFKkgDj6z.png)
该仓库主要整理工作中常见的绘图工作，当需要进行数据批量绘图时可以结合数据批处理实现。部分产品数据使用模拟数据实现，开源绘图代码。权作整理汇总之用。代码用`jupyter`支持。
+ :+1:代码模板性比较强，对同种数据结构支撑较好
+ :-1:数据结构发生变化，则对应的代码需要调整
+ :exclamation:图片均已链接到源码

**:memo:阅读目录**
<!-- TOC orderedList:false -->

- [日常工作中的绘图-Python实现](#日常工作中的绘图-python实现)
    - [常规绘图](#常规绘图)
        - [时间序列绘图](#时间序列绘图)
        - [柱形图](#柱形图)
        - [箱图](#箱图)
        - [组分饼图](#组分饼图)
        - [直方图](#直方图)
    - [非常规绘图](#非常规绘图)
        - [双Y轴同比柱状图](#双y轴同比柱状图)
        - [共享X轴的时间序列图](#共享x轴的时间序列图)
        - [为绘图添加背景色](#为绘图添加背景色)
        - [为常规点图增加伪彩色](#为常规点图增加伪彩色)
        - [常规参数复合绘图](#常规参数复合绘图)
        - [堆叠图（模拟重构）](#堆叠图模拟重构)
        - [特征雷达图](#特征雷达图)
        - [日历图](#日历图)
            - [日历热力图](#日历热力图)
            - [自定义标签日历图](#自定义标签日历图)
            - [基于pyecharts实现日历图](#基于pyecharts实现日历图)
        - [玫瑰图](#玫瑰图)
        - [雷达产品伪彩图](#雷达产品伪彩图)
    - [地理绘图](#地理绘图)
    - [动态绘图](#动态绘图)
    - [tips](#tips)
        - [华夫饼图](#华夫饼图)

<!-- /TOC -->
## 常规绘图
### 时间序列绘图
+ :house:常规时间序列绘图
文件原地址包含快速绘制的方法`pd.DataFrame.plot`
[![常规时间序列](https://i.loli.net/2020/07/29/RomOTl3ScVrgW4u.png)](../PlotInWork/时间序列.ipynb)
### 柱形图
+ :rocket:实现条形图堆叠
+ :fire:实现纵向与横向条形图绘制
<figure class='half'>
    <a href='../PlotInWork/common.ipynb'>
    <img src='https://i.loli.net/2020/07/31/KOMfY98UIQdNhEF.png' width='50%'></a><a href='../PlotInWork/common.ipynb'><img src='https://i.loli.net/2020/07/31/Bz2TZ86dsyp1Rvh.png' width='50%'></a>
</figure>&ensp;

### 箱图
[![box](https://i.loli.net/2020/07/31/TKSuEwyh3FbDlnm.png)](../PlotInWork/common.ipynb)
### 组分饼图
<figure class='half'>
    <a href='../PlotInWork/饼图.ipynb'><img src='https://i.loli.net/2020/08/04/DY4VHKqeN6UkaJv.png' width='40%'></a><a href='../PlotInWork/饼图.ipynb'><img src='https://i.loli.net/2020/08/04/hozA3uPIncGLQ2J.png' width='60%'></a>
</figure>

### 直方图
[![](https://i.loli.net/2020/07/31/9NhC2evdHTEjkrU.png)](../PlotInWork/common.ipynb)

***
## 非常规绘图
### 双Y轴同比柱状图
+ :fire:CO数据独立一个Y轴，不至于信息被遮挡
+ :rocket:实现柱状图数据标记
+ :basketball:在标签及其他文本中使用`latex`表述
[![双Y同比图](https://i.loli.net/2020/07/28/kbTJK5IPlMvi3Ls.png)](../PlotInWork/双Y轴同比数据绘制.ipynb)
### 共享X轴的时间序列图
+ :fire:时间轴定制标签
+ :smile:共享X轴，并调整子图间距
[![共享X轴时间序列](https://i.loli.net/2020/07/29/GgO6j3yRLFUdAZE.png)](../PlotInWork/时间序列.ipynb)
### 为绘图添加背景色
[![](https://i.loli.net/2020/07/30/h4HnsUKNbaJMBAu.png)](../PlotInWork/plotInimage.ipynb)
### 为常规点图增加伪彩色
+ :rocket:点位置信息+点尺寸信息+点颜色信息

<figure class='half'>
    <a href='../PlotInWork/ScatterColorPlot.ipynb'><img src='https://i.loli.net/2020/07/31/M6xHDcmNigh8l5O.png' width='60%'><a href='../PlotInWork/ScatterColorPlot.ipynb'><img src='https://i.loli.net/2020/07/31/ySDhIwZNOT4517u.png' width='40%'></a>
</figure>

### 常规参数复合绘图
+ :heavy_check_mark:实现风向风速绘制
+ :heart:实现定义坐标轴颜色
+ :joy:代码过于冗长，好在可以套用数据模板实现调用简化
[![常规参数](https://i.loli.net/2020/08/13/Glzq8Fgfc9vXNWh.png)](../PlotInWork/常规六参数.ipynb)
### 堆叠图（模拟重构）
+ :lemon:组分堆叠
+ :tomato:堆叠加折线图模拟重构
+ :hamburger:图例及封装重置X轴标签
[![堆叠图](https://i.loli.net/2020/07/29/U7aYvIT2dANeQtn.png)](../PlotInWork/模拟组分重构-堆叠图.ipynb)
+ :fire: 基于时间序列堆叠和数据处理绘制百分比堆叠
[![百分比堆叠](https://i.loli.net/2020/07/29/jMp1fv7J2QZmTkH.png)](../PlotInWork/模拟组分重构-堆叠图.ipynb)

### 特征雷达图
+ :fire:简单雷达图到特征雷达图绘制
+ :apple:使用极坐标绘制实现
+ :rocket:整理数据集可以实现批量绘制特征雷达图
<figure class='half'>
    <a href='../PlotInWork/特征雷达绘图.ipynb'><img src = 'https://i.loli.net/2020/07/30/3EfwIRhsQmMv1cl.png' width='50%'></a><a href='../PlotInWork/特征雷达绘图.ipynb'><img src = "https://i.loli.net/2020/07/30/ivP3Ga941e7zRN8.png" width='50%'></a>
</figure>

### 日历图
#### 日历热力图
+ :fire:基于seaborn实现
+ :rocket:自定义颜色及颜色值的映射区间
[![日历热力图](https://i.loli.net/2020/07/30/tGyj3WxIcYH6pMS.png)](../PlotInWork/日历图.ipynb)
#### 自定义标签日历图
+ :calendar: 实现比较底层与简单
+ :fire:实现colorbar自定义及位子调整
[![标签热力图](https://i.loli.net/2020/07/30/QaPOj8WVXdAxkDt.png)](../PlotInWork/日历图.ipynb)
#### 基于pyecharts实现日历图
+ :fire:实现动态交互
[![](https://i.loli.net/2020/07/30/YRqkhN3Dwylxg2T.png)](../PlotInWork/日历图.ipynb)
[![](https://i.loli.net/2020/07/30/zUJK8EBIvmbCyqd.png)](../PlotInWork/日历图.ipynb)

### 玫瑰图
+ :rose:实现风频统计及玫瑰图绘制
+ :fire:利用等高线实现差值绘制污染玫瑰图
<figure class='half'>
    <a href='../PlotInWork/WindRose.ipynb'><img src='https://i.loli.net/2020/07/30/AydcLhuiYDxmG3p.png' width='50%'></a><a href='../PlotInWork/WindRose.ipynb'><img src='https://i.loli.net/2020/07/30/P8gr5N3MU6vQOcJ.png' width='50%'></a>
</figure>

### 雷达产品伪彩图
+ :pencil:实现盲区过滤
+ :rocket:可选择图片绘制高度上限（5Km）
+ :football:伪彩图cmap参数自定义
+ :fire:支持图片保存
<br>[![lidar](https://i.loli.net/2020/07/29/St5pxyTzGahwjoO.png)](../PlotInWork/伪彩图绘制.ipynb)
+ :rocket:使用等高线绘图，绘制扫描雷达图
+ :football:使用绘制图片来实现扫描雷达伪彩图绘制，且可将该思路用于绘制污染玫瑰图
<figure class='half'>
    <a href='../PlotInWork/伪彩图绘制.ipynb'><img src='https://i.loli.net/2020/07/30/tYafCRJLm16VpwS.png' width='50%'></a><a href='../PlotInWork/伪彩图绘制.ipynb'><img src='https://i.loli.net/2020/07/30/zEilPAYMu5sbqjF.png' width='50%'></a>
</figure>

***

## 地理绘图
+ :fire:地图信息交互
+ :-1: 通过模拟数据实现原理
+ :rose: 通过html字体实现中文标签
[![folium](https://i.loli.net/2020/08/06/CP9Z4J7we1piLfE.jpg)](../PlotInWork/folium绘制地理图.ipynb)
***
## 动态绘图
***
## tips
### 华夫饼图
+ :green_apple:支持在线多种图标
+ :christmas_tree:支持自定义图例
[![](https://i.loli.net/2020/07/31/wuKY1kHTUIPFWSn.png)](../PlotInWork/WaffleInPython.ipynb)
[![](https://i.loli.net/2020/07/31/SJDrowxpQMZEHOi.png)](../PlotInWork/WaffleInPython.ipynb)