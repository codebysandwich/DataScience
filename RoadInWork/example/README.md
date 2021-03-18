# 工作中的数据处理范例
## 将雷达导出的边界层数据提取并做小时均值处理。

:warning:存在两种导出的结果：
![](https://i.loli.net/2021/03/18/dP7RGXNvL3U6qja.png)
![](https://i.loli.net/2021/03/18/fLQ9tqWzAJ7bv45.png)

:warning:边界层数据存在`,`分隔的数据需要处理成均值的情况。例如0.795,0.945处理成0.87，且分隔数据的数量不定，可能是两个数据也可能是三个建议的边界层数据，需要将其提取出来做均值处理。
![](https://i.loli.net/2021/03/18/t1WyVdMom3ALFYq.png)

:memo:处理后的结果示例：
![](https://i.loli.net/2021/03/18/TrfgbR3yOuV8cIz.png)
