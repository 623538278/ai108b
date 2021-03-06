10-機器學習
===
簡介
---
機器學習(ML)是對演算法和統計模型的科學研究，電腦系統使用這些演算法和模型來執行特定任務，而不使用明確的指令，而是依靠模式和推斷。它被視為人工智慧的一個子集。機器學習演算法基於樣本數據(即所謂的“訓練數據”)建立數學模型，以便做出預測或決策，而無需經過明確的編程來執行任務。機器學習演算法被廣泛應用於各種應用中，如電子郵件過濾和電腦視覺，在這些應用中，開發一種有效執行任務的傳統演算法是困難的或不可行的。
*****
機率式算法
----
以下内容摘自老師筆記<br>
### 蒙地卡羅演算法 (Monte Carlo Algorithm)
利用亂數隨機抽樣的方式以計算某種解答的演算法，被稱為蒙地卡羅演算法，其中最簡單的方法是直接取樣算法。
<br>
舉例而言，假如我們不知道半徑為 1 的圓形面積，那麼就可以利用亂數隨機取樣 1百萬個 X=random[-1...1], Y=random[-1...1] 之間的的值，然後看看有多少點落在 
<br>
x2+y2<=1
<br>
 的範圍之內 P(in circle)。最後利用 4 * P(in circle) 就可以計算出該圓形的面積。
 <br>
 
 ### 最大概似估計
 對於任何一個隨機現象，我們可以用隨機變數 X 描述，假設樣本 x 的機率分布以 p(x)表示。<br>
假如經過觀察之後，經由觀察數據x1,x2,⋯,xn的統計，得到其分布為 p'(x) ，於是我們就可以利用機率分布 p' 反推出 p 。<br>
一個最簡單的想法是 p(x) = p'(x) ，也就是這些觀察是具有代表性的，於是統計上的機率分布符合真實的機率分佈。
這個想法的背後，其實是有理論基礎的，其理論稱為「最大似然法則」或「最大概似估計」 (Maximum Likelihood Estimation)。
<br>

### 最大概似估計的數學想法
隨然我們觀察到的統計現象是 p'，但是真正的 p 卻有無限多種可能，基本上任何機率分布都可能產生觀察現象 p'。
即便如此，每一個機率分布 p 會產生觀察現象 p' 的可能性卻大有不同，假如機率模型 p 與 p'(x) 的分布一致 ，那麼 p 產生 p'(x) 現象的機率將會是最大的。
因此，設定 p(x) = p'(x) 的想法，其背後的目標乃是要最大化機率源模型 p 產生 p' 現象的可能性，這個最大化的目標就稱為「最大概似估計」。

參考資料
----
[機器學習](https://misavo.com/blog/陳鍾誠/書籍/人工智慧/10-機器學習)
