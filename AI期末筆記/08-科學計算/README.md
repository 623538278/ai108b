08-科學計算——使用Python
======
簡介
----
電腦就是《計算機》，而數學則是《計算的學問》，這樣說來，電腦應該是數學的實驗場！
<br>
科學計算 -- 大至上就是拿電腦來進行數學計算、探索、實驗的一個領域。經典數學大致可以分為下列領域
<br>
代數 -- 數論、方程式、抽象代數、線性代數、...<br>
幾何 -- 歐氏幾何、非歐幾何、拓譜學、微分幾何 ....<br>
微積分 -- 又被稱為分析學，包含微分方程、級數與轉換等等 ...<br>


但是那些沒納入經典數學領域的，還有<br>
機率統計<br>
集合論<br>
邏輯推論<br>
圖形理論<br>
...<br>
******
數學證明是甚麼？
-----
想要理解甚麼是數學，最快速的捷徑是從公理系統下手，因為公理系統是數學證明的核心，理解了公理系統之後，就可以看懂數學家到底在玩甚麼遊戲了！
<br>
但是、很多數學的公理系統太過複雜，因此很難解釋，讀者往往在還沒入門之前，就已經先恍神了，所以為了讓大家很容易的理解公理系統，我們選擇了一個最簡單的數學體系，那就是布林邏輯。
<br>
布林邏輯只有兩個值，那就是 0 與 1 ，所以可以說是最簡單的數學體系了，就讓我們從布林邏輯開始，理解何謂公理系統吧！<br>
******
科學計算套件
------
### numpy -- 數值陣列
[numpy -- 數值陣列](https://numpy.org/)
<br>
### scipy -- 科學計算
[scipy -- 科學計算](https://www.scipy.org/)
<br>
### Sympy -- 符號運算
[Sympy -- 符號運算](https://www.sympy.org/en/index.html)
<br>
### matplotlib -- 繪圖套件
[matplotlib -- 繪圖套件](https://matplotlib.org/)
<br>
### Panda -- 資料分析
[Panda -- 資料分析](https://pandas.pydata.org/)
<br>
### 套件安裝
```$ pip install numpy
$ pip install matplotlib
$ pip install scipy
$ pip install panda
$ pip install sympy
$ pip install opencv-contrib-python // 之後使用 import cv2 (精簡版 pip install opencv-python)
$ pip install opencv-contrib-python-headless // opencv 的視窗介面 (精簡版 pip install opencv-python-headless)
```
*****
範例程式
----
以下程式未修改其理解OK
<br>
[root](https://github.com/623538278/ai108b/blob/master/AI期末筆記/08-科學計算/root.py)
<br>
[result](https://github.com/623538278/ai108b/blob/master/AI期末筆記/08-科學計算/result1.md)
<br>
*****
[simplify](https://github.com/623538278/ai108b/blob/master/AI期末筆記/08-科學計算/simplify1.py)
<br>
[result](https://github.com/623538278/ai108b/blob/master/AI期末筆記/08-科學計算/result2.md)
<br>
****
參考資料
----
[範例程式](https://misavo.com/blog/陳鍾誠/書籍/科學計算)
<br>
[科學計算](https://misavo.com/blog/陳鍾誠/書籍/科學計算)
<br>
