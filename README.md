# 大学物理实验不确定度计算

教材：《大学物理实验》（上海交通大学出版社2017年8月第1版）

## A 类标准不确定度评定

对直接测量来说，如果在相同条件下对某物理量 $X\text{进行了}_n$
次独立重复测量，其测量值分别为 $x_1,x_2,x_3,\cdots,x_n$ ,用 $\overline{x}$ 来表示平均值，则

$$\overline{x}=\frac{1}{n}(x_{1}+x_{2}+x_{3}+\cdots+x_{n})=\frac{1}{n}\sum_{i=1}^{n}x_{i}$$

$s(x_i)$ 为某次测量的实验标准偏差，由贝塞尔公式计算得到

$$s(x_i)=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\overline{x})^2}$$

由于多次测量的平均值比一次测量值更淮确，随着测量次数的增多，平均值收敛于期望值。因此，通常以样本的算术平均值 $\bar{x}$ 作为被测量值的最佳值， $s(\bar{x})$ 为平均值的实验标准差， 其值为：

$$s(\overline{x})=\frac{s(x_i)}{\sqrt{n}}$$

通常 A 类标准不确定度由标准偏差 $s(x_i)$ 乘以 $\dfrac{t}{\sqrt n}$ 得到，即

$$u_A = \dfrac{t}{\sqrt {n}} \sqrt {\frac{1}{n - 1} \sum_{i=1}^{n}(x_{i} - \overline{x}) ^{2}}= \frac{t}{\sqrt{n}} s(x_i)$$

在大多数普通物理实验教学中，为了简便起见，一般就取 $\dfrac{t}{\sqrt n} \thickapprox 1$ , 即

$$u_A = s(x_i)$$

## 合成标准不确定度评定

对于受多个误差来源影响的某直接测量量，被测量量 $X$ 的不确定度可能不止一项，设其有 $k$ 项，且各不确定度分量彼此独立，其协方差为零，则用方和根方式合成，称合成标准不确定度 $u_C$

$$u_C = \sqrt{\sum_{i=1}^k u_i^2}$$

## 间接测量量不确定度的评定

设间接测量量 $N$ 是由直接测量量 $x,y,z\cdots$ 通过函数关系 $N=f(x,y,z\cdots)$ 计算得到的，其中 $x,y,z\cdots$ 是彼此独立的直接测量量。设 $x,y,z\cdots$ 的不确定度分别为 $u_x,u_y,u_z\cdots$ ，它们必然会影响间接测量结果，使 $N$ 也有相应的不确定度。由于不确定度是微小的量，相当于数学中的“增量”，因此间接测量的不确定度的计算公式与数学中的全微分公式类似。考虑到用不确定度代替全微分，以及不确定度合成的统计性质，可以用下式来简化计算间接测量量 $N$ 的不确定度 $u_N$ 。

$$u_{N}=\sqrt{\left(\frac{\partial f}{\partial x}\right)^{2}\cdot u_{x}^{2}+\left(\frac{\partial f}{\partial y}\right)^{2}\cdot u_{y}^{2}+\left(\frac{\partial f}{\partial z}\right)^{2}\cdot u_{z}^{2}+\cdots}$$
