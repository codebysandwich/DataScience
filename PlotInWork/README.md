<!--
 * @Author: sandwich
 * @Date: 2020-07-28 09:05:08
 * @LastEditTime: 2020-07-30 00:59:54
 * @LastEditors: sandwich
 * @Description: 工作绘图开源文档
 * @FilePath: /DataScience/PlotInWork/README.md
--> 
# 日常工作中的绘图-Python实现
![logo](https://i.loli.net/2020/07/28/X5WEUHuFKkgDj6z.png)
该仓库主要整理工作中常见的绘图工作，当需要进行数据批量绘图时可以结合数据批处理实现。部分产品数据使用模拟数据实现，开源绘图代码。权作整理汇总之用。代码用`jupyter`支持。
+ :+1:代码模板性比较强，对同种数据结构支撑较好
+ :-1:数据结构发生变化，则对应的代码需要调整
## 常规绘图
### 时间序列绘图
+ :house:常规时间序列绘图
文件原地址包含快速绘制的方法`pd.DataFrame.plot`
[![常规时间序列](https://i.loli.net/2020/07/29/RomOTl3ScVrgW4u.png)](../PlotInWork/时间序列.ipynb)
### 柱形图
### 组分饼图
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
<!-- <figure class='half'>
    <a href='../PlotInWork/特征雷达绘图.ipynb'>
    <img src = 'https://i.loli.net/2020/07/30/3EfwIRhsQmMv1cl.png' width = '50%' align = left>
    </a>
    <a href='../PlotInWork/特征雷达绘图.ipynb'>
    <img src = "https://i.loli.net/2020/07/30/ivP3Ga941e7zRN8.png" width='50%' align = right>
    </a>
</figure>&ensp; -->
![](https://i.loli.net/2020/07/30/3EfwIRhsQmMv1cl.png)![](https://i.loli.net/2020/07/30/ivP3Ga941e7zRN8.png)

### 雷达产品伪彩图
+ :pencil:实现盲区过滤
+ :rocket:可选择图片绘制高度上限（5Km）
+ :football:伪彩图cmap参数自定义
+ :fire:支持图片保存
<br>[![lidar](https://i.loli.net/2020/07/29/St5pxyTzGahwjoO.png)](../PlotInWork/伪彩图绘制.ipynb)
## 地理绘图
## 动态绘图
## tips