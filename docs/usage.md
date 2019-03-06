VisualNN是用于可视化建模神经网络的工具, 并提供模型导入导出, 在线训练的功能, 具体界面如下

# 界面介绍
整个网站的界面如下所示, 主要组成有三个部分, 左侧是神经网络单元工具箱, 中间是神经网络架构图, 右侧是网络单元参数设置界面, 可以通过拖拉拽左侧的网络单元到中间来自行搭建神经网络模型, 也可以导入系统提供的很多经典模型. 下面分节讲述每个部分的使用方法.

![](./picture/screenshot.png)
## 1. 工具栏介绍

具体的工具栏如下图所示, 从左到右分别提供了model zoo, load from text, export, import的功能.



![](./picture/toolbar.png)

* model zoo

model zoo使得用户能够直接导入一些已经设计好的经典模型, 具体界面如下所示, 目前系统还处于原型阶段, 尚未提供网络结构.

![](./picture/model_zoo.png)

* load from text

这项功能使得用户可以通过json格式或者pb格式的输入直接导入网络结构, 具体界面如下所示:

![](./picture/load_from_text.png)

* export功能
  

用户可以通过export按钮从磁盘导入json或者pbtxt格式的模型文件, 如下图

![](./picture/export.png)

* import功能

用户可以通过import按钮将网页中设计好的神经网络文件导出为json或者pbtxt格式的文件输出到磁盘上, 如下图所示

![](./picture/import.png)

## 2. 神经网络基本单元

VisualNN提供一些基本的网络单元来进行神经网络设计, 具体界面如下

![](./picture/network_unit.png)

从上到下分别由Data, Vision, Recurrent, Utility, Activation, Normalization, Common, Noise, Loss, Wrapper构成.

* data层

data层主要用于定义神经网络输入的格式, 如下图所示

![](./picture/data.png)


* vision层

Vision层包含了计算机视觉常用的一些单元, 如下图所示

![](./picture/vision.png)

下面介绍一些常用的组件

![](./picture/recurrent.png)

