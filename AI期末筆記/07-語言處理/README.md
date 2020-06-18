07-語言處理
===
前言
---
語言處理是電腦科學領域與人工智慧領域中的一個重要方向。它研究能實現人與電腦之間用自然語言進行有效通信的各種理論和方法。自然語言處理是一門融語言學、電腦科學、數學於一體的科學。因此，這一領域的研究將涉及自然語言，即人們日常使用的語言，所以它與語言學的研究有著密切的聯繫，但又有重要的區別。自然語言處理並不是一般地研究自然語言，而在於研製能有效地實現自然語言通信的電腦系統，特別是其中的軟體系統。因而它是電腦科學的一部分。
<br>
自然語言處理（NLP）是電腦科學，人工智慧，語言學關注電腦和人類（自然）語言之間的相互作用的領域。
****
簡介
---
語言是人類區別其他動物的本質特性。在所有生物中，只有人類才具有語言能力。人類的多種智能都與語言有著密切的關係。人類的邏輯思維以語言為形式，人類的絕大部分知識也是以語言文字的形式記載和流傳下來的。因而，它也是人工智慧的一個重要，甚至核心部分。
<br>
用自然語言與電腦進行通信，這是人們長期以來所追求的。因為它既有明顯的實際意義，同時也有重要的理論意義：人們可以用自己最習慣的語言來使用電腦，而無需再花大量的時間和精力去學習不很自然和習慣的各種電腦語言；人們也可通過它進一步瞭解人類的語言能力和智能的機制。
***
發展歷史
---
最早的自然語言理解方面的研究工作是機器翻譯。1949年，美國人威弗首先提出了機器翻譯設計方案。20世紀60年代，國外對機器翻譯曾有大規模的研究工作，耗費了巨額費用，但人們當時顯然是低估了自然語言的複雜性，語言處理的理論和技術均不成熱，所以進展不大。主要的做法是存儲兩種語言的單詞、短語對應譯法的大辭典，翻譯時一一對應，技術上只是調整語言的同條順序。但日常生活中語言的翻譯遠不是如此簡單，很多時候還要參考某句話前後的意思。大約90年代開始，自然語言處理領域發生了巨大的變化。這種變化的兩個明顯的特徵是：
<br>
（1）對系統輸入，要求研製的自然語言處理系統能處理大規模的真實文本，而不是如以前的研究性系統那樣，只能處理很少的詞條和典型句子。只有這樣，研製的系統才有真正的實用價值。<br>
（2）對系統的輸出，鑒於真實地理解自然語言是十分困難的，對系統並不要求能對自然語言文本進行深層的理解，但要能從中抽取有用的資訊。例如，對自然語言文本進行自動地提取索引詞，過濾，檢索，自動提取重要資訊，進行自動摘要等等。<br>
同時，由於強調了“大規模”，強調了“真實文本”，下麵兩方面的基礎性工作也得到了重視和加強。
<br>
（1）大規模真實語料庫的研製。大規模的經過不同深度加工的真實文本的語料庫，是研究自然語言統計性質的基礎。沒有它們，統計方法只能是無源之水。<br>
（2）大規模、資訊豐富的詞典的編制工作。規模為幾萬，十幾萬，甚至幾十萬詞，含有豐富的資訊（如包含詞的搭配資訊）的電腦可用詞典對自然語言處理的重要性是很明顯的。
******
相關技術
----
### Add-one（Laplace） Smoothing
加一平滑法，又稱拉普拉斯定律，其保證每個n-gram在訓練語料中至少出現1次，以bigram為例，
<br>
公式如圖：<br>
<img style="width:250px;height:64px;" alt="公式" src="https://bkimg.cdn.bcebos.com/pic/54fbb2fb43166d2202f3c80d452309f79152d2a7?x-bce-process=image/resize,m_lfit,w_250,h_250,limit_1">
<br>
其中，V是所有bigram的個數。
<br>
### Good-Turing Smoothing
其基本思想是利用頻率的類別資訊對頻率進行平滑。調整出現頻率為c的n-gram頻率為c*
<br>
<img style="width:250px;height:52px;" alt="公式" src="https://bkimg.cdn.bcebos.com/pic/55e736d12f2eb9380c57a66bd6628535e5dd6f75?x-bce-process=image/resize,m_lfit,w_250,h_250,limit_1">
<br>
直接的改進策略就是“對出現次數超過某個閾值的gram，不進行平滑，閾值一般取8~10”，
<br>
### InterpolationSmoothing
不管是Add-one，還是Good Turing平滑技術，對於未出現的n-gram都一視同仁，難免存在不合理（事件發生概率存在差別），所以這裏再介紹一種線性插值平滑技術，其基本思想是將高階模型和低階模型作線性組合，利用低元n-gram模型對高元n-gram模型進行線性插值。因為在沒有足夠的數據對高元n-gram模型進行概率估計時，低元n-gram模型通常可以提供有用的資訊。公式如下圖：<br>
<img style="width:250px;height:62px;" alt="Interpolation Smoothing" src="https://bkimg.cdn.bcebos.com/pic/203fb80e7bec54e7a255c687ba389b504ec26aea?x-bce-process=image/resize,m_lfit,w_250,h_250,limit_1">
<br>
擴展方式為如圖：<br>
λs可以通過EM演算法來估計，具體步驟如下：<br>
<img style="width:250px;height:63px;" alt="扩展方式" src="https://bkimg.cdn.bcebos.com/pic/f603918fa0ec08fa159dcf3e5aee3d6d54fbda8e?x-bce-process=image/resize,m_lfit,w_250,h_250,limit_1">
<br>
首先，確定三種數據：Training data、Held-out data和Test data；<br>
然後，根據Training data構造初始的語言模型，並確定初始的λs（如均為1）；<br>
最後，基於EM演算法迭代地優化λs，使得Held-out data概率最大化。<br>
*****
範例程式與作業練習
----
(其中範例程式為老師上課筆記內容)<br>
[eliza](https://misavo.com/blog/陳鍾誠/書籍/人工智慧/07-語言處理/C2-Eliza交談系統)<br>
[作業](https://github.com/623538278/ai108b/blob/master/HW6.py)<br>
[作業運行結果](https://github.com/623538278/ai108b/blob/master/HW6.result)<br>
*****
參考資料
----
[自然語言處理](https://baike.baidu.com/item/自然语言处理)<br>
[Add-one（Laplace） Smoothing](https://baike.baidu.com/item/自然语言处理)<br>
[Good-Turing Smoothing](https://baike.baidu.com/item/自然语言处理)<br>
[InterpolationSmoothing](https://baike.baidu.com/item/自然语言处理)<br>
[範例程式](https://misavo.com/blog/陳鍾誠/書籍/人工智慧/07-語言處理/C2-Eliza交談系統)<br>


