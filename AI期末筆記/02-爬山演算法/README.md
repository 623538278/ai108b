02-爬山演算法
=====
簡介
-----
爬山算法是local search(局部搜索)算法中最简单的一种。当我们遇到的问题的解空间很大时，我们想从中直接获取最优解是很耗时间的。但是，我们可以做到的是，我们可以从一个小的解空间短时间获得最优解，这就是local search算法的核心。
*******
爬山演算法
-----
```Algorithm Hill-Climbing(pi)
  p = pi // 設定粒子 p 為起始粒子 pi
  while not isEnd()
    pn = move(p) //選擇粒子p的鄰居pn
    if pn.energy()<=p.energy() //能量更低，就接受
      p = pn;
End Algorithm
```
<br>
（該段程式碼出自https://blog.csdn.net/GarfieldEr007/article/details/51244582）

梯度下降法
----
<br>
梯度下降方法基于以下的观察：如果实值函数 F[X] 在点 a 处可微且有定义，那么函数F[X]  在a  点沿着梯度相反的方向  下降最快。
因而，如果
<img title="" align="absmiddle" class="J-formula-img" style="vertical-align:-0.755ex;width:16.771ex;height:2.634ex;" alt="" src="https://bkimg.cdn.bcebos.com/formula/b76f577d8222abbc8e3b03bcca625ab0.svg" data-height="21" data-width="134" data-png="https://bkimg.cdn.bcebos.com/formula/b76f577d8222abbc8e3b03bcca625ab0.png">
对于 <img title="" align="absmiddle" class="J-formula-img" style="vertical-align:-0.755ex;width:5.523ex;height:2.509ex;" alt="" src="https://bkimg.cdn.bcebos.com/formula/f99569b57b4ba0fe82462c9fca18990f.svg" data-height="20" data-width="44" data-png="https://bkimg.cdn.bcebos.com/formula/f99569b57b4ba0fe82462c9fca18990f.png"> 为一个够小数值时成立，那么  。
考虑到这一点，我们可以从函数F的局部极小值的初始估计X0  出发，并考虑如下序列 X1,X2,X3..... 使得<img title="" align="absmiddle" class="J-formula-img" style="vertical-align:-0.755ex;width:31.107ex;height:2.634ex;" alt="" src="https://bkimg.cdn.bcebos.com/formula/e1d7cac60abe2106768fb108d6494fb5.svg" data-height="21" data-width="249" data-png="https://bkimg.cdn.bcebos.com/formula/e1d7cac60abe2106768fb108d6494fb5.png">
 
因此可得到<img title="" align="absmiddle" class="J-formula-img" style="vertical-align:-0.755ex;width:31.098ex;height:2.634ex;" alt="" src="https://bkimg.cdn.bcebos.com/formula/5929a0255e220125c6f9da620f9c651c.svg" data-height="21" data-width="249" data-png="https://bkimg.cdn.bcebos.com/formula/5929a0255e220125c6f9da620f9c651c.png">
 
　　
 
如果顺利的话序列 Xn收敛到期望的极值。注意每次迭代步长可以改变。
右侧的图片示例了这一过程，这里假设F定义在平面上，并且函数图像是一个碗形。蓝色的曲线是等高线（水平集），即函数F为常数的集合构成的曲线。红色的箭头指向该点梯度的反方向。（一点处的梯度方向与通过该点的等高线垂直）。沿着梯度下降方向，将最终到达碗底，即函数F值最小的点。

（參閱自Avriel, Mordecai (2003). Nonlinear Programming: Analysis and Methods. Courier Corporation. ISBN 978-0-486-43227-4.）
<br>
******
範例程式練習及作業
------
[作業1](https://github.com/623538278/ai108b/blob/master/net3.py)<br>
[結果1](https://github.com/623538278/ai108b/blob/master/net3%20result)<br>
[作業2](https://github.com/623538278/ai108b/blob/master/HW1.py)<br>
[結果2](https://github.com/623538278/ai108b/blob/master/HW1.RESULT)<br>
（以上內容皆已理解）<br>
*******
參考資料
-----
[梯度下降法](https://baike.baidu.com/item/梯度下降法)<br>
[爬山演算法](https://jvruo.com/archives/604/)
