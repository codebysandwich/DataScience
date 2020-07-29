<!--
 * @Author: sandwich
 * @Date: 2020-07-28 09:05:08
 * @LastEditTime: 2020-07-29 14:06:08
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
### 雷达产品伪彩图
+ :pencil:实现盲区过滤
+ :rocket:可选择图片绘制高度上限（5Km）
+ :football:伪彩图cmap参数自定义
+ :fire:支持图片保存
<br>[![lidar](https://i.loli.net/2020/07/29/St5pxyTzGahwjoO.png)](../PlotInWork/伪彩图绘制.ipynb)
## 地理绘图
## 动态绘图
## tips