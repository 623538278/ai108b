11-深度學習
====
簡介
---
深度學習(DL, Deep Learning)是機器學習(ML, Machine Learning)領域中一個新的研究方向，它被引入機器學習使其更接近於最初的目標——人工智慧(AI, Artificial Intelligence)。
<br>
深度學習是學習樣本數據的內在規律和表示層次，這些學習過程中獲得的資訊對諸如文字，圖像和聲音等數據的解釋有很大的幫助。它的最終目標是讓機器能夠像人一樣具有分析學習能力，能夠識別文字、圖像和聲音等數據。 深度學習是一個複雜的機器學習演算法，在語音和圖像識別方面取得的效果，遠遠超過先前相關技術。  
<br>
深度學習在搜索技術，數據挖掘，機器學習，機器翻譯，自然語言處理，多媒體學習，語音，推薦和個性化技術，以及其他相關領域都取得了很多成果。深度學習使機器模仿視聽和思考等人類的活動，解決了很多複雜的模式識別難題，使得人工智慧相關技術取得了很大進步。 
<br>
*****
實作——使用WEKA進行數據探勘
-----
### 什麼是資料探勘
資料探勘一般是指從大量的數據中自動搜索隱藏於其中的有著特殊關係性資訊的過程。資料探勘通常與電腦科學有關，並通過統計、線上分析處理、等諸多方法來實現上述目標。
<br>
資料探勘過程的總體目標是從一個資料集中提取資訊，並將其轉換成可理解的結構，以進一步使用。整體上來講，資料探勘屬於大數據分析的一種方式，它可以對一樣事物的過去，現在，未來的行為或資訊進行分析來推導出它的過去或未來。
<br>
### Weka 是...?
Weka (Waikato Environment for Knowledge Analysis)，是一套提供資料探勘以及機器學習的一套軟體,WeKa的全名是懷卡托智能分析環境,它和它的源代碼可在其官方網站下載。
<br>
WeKa作為一個公開的數據挖掘工作平臺，集合了大量能承擔數據挖掘任務的機器學習演算法，包括對數據進行預處理，分類，回歸、聚類、聯結以及在新的互動式介面上的可視化。<br>
![weka GUI 界面](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3BGZEV5YJOlhq1a5WICt3w03cyEeyJQRLnMEiZCOI7*q920kjLnnFTJnFcTyjIfRWQ!!/m&ek=1&kp=1&pt=0&bo=jgHvAAAAAAARF0A!&tl=1&vuin=623538278&tm=1592546400&sce=60-4-3&rf=0-0)
<br>
### 目的
用Weka對資料集進行分群與分類<br>
採用的資料集為加州大學爾灣分校所提供的 "zoo.dataset"<br>
### 原始資料
![原始資料](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3DB*ZXdFzn1vu8xCq4lnPzwgaiiXAIGv8d8tilxC9PvU0XbSzaStu4AwMQ2tle4MWw!!/m&ek=1&kp=1&pt=0&bo=MAFxAAAAAAARF2A!&tl=1&vuin=623538278&tm=1592546400&sce=60-3-3&rf=0-0)
<br>
另存後用 excel 開啟，對照它提供的另一個檔案 "zoo.name" 中各個欄位的說明，手動添加後原本看不懂的密碼變成美麗的表格：
<br>
![表格](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3EmRcGstKLNc0IeO3tBxaPEJ4AxfOwB.KG29UIEtsU4VGJBlk98vgqsfQXsweXHJ6w!!/m&ek=1&kp=1&pt=0&bo=qAT7AAAAAAARF3c!&tl=1&vuin=623538278&tm=1592546400&sce=60-4-3&rf=0-0)
<br>
此資料集是針對動物園裡的動物們去分析各項特徵，最後一行 type (1~7) 代表的是它們在生物學上的分類。除了第 1 行姓名是文字、第 14 行的 legs 是間斷型資料，其餘欄位都用 Boolean 值來呈現，1 代表「是」或「有」， 0 代表「否」或「無」。<br>
### 分群 （Clustering）
分群的概念是將一群雜亂、沒有標籤的資料，利用它各個屬性資料的不同去分類。就像把有羽毛的和沒有羽毛的、兩隻腳和四隻腳的做出區別。理想的分群會使「單一群體內」的特徵相似，讓「不同群之間」的差異放大。
<br>
#### 分群——K 平均法 （K-means）
K 平均法的理念是將所有資料都分到 K 個群之中。先設定好你希望分幾個群之後，電腦會先隨機給定 K 個點的位置作為群中心。<br>
1.將其餘的所有點歸類到離它距離最近的群中心。<br>
2.最後再取出每個群內樣本們的中心點做為新的群中心。<br>
以上兩點會循環進行，直到群中心的位置不再變動。<br>
![K-means](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3BQ9bY1*trkNah7Qt07vsUchZAybp7qOoFYV3k9R491kHkN3M6D9m4q*dzP7fdD2lA!!/m&ek=1&kp=1&pt=0&bo=0gJzAQAAAAADF5A!&tl=1&vuin=623538278&tm=1592546400&sce=60-4-3&rf=0-0)
<br>
從上圖可以看到，原本的 Full Data 共 100 種動物被依照 16 個項目的差異分出 7 個群，其中除了 leg 欄位以外都是介於 0~1 的正數，代表的是在這個群之中有多少比例的動物符合該特徵。<br>
舉個例子：第二列的 feather （是否有羽毛），只有3 內的動物有此特徵，且通通都有！就可以輕鬆的推斷出 3 是鳥類啦。<br>
### 分類（Classification）
不同於分群將性質相似的資料匯聚在一起，分類則是利用已知的資料（有飆上類別的）去建構分類模型，讓我們有一個準則去推論已知或是未來新加入的資料的分類。
<br>
#### 分類——決策樹（Decision Tree）
![tree](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3EWmCwZV4M52IjWIap9r8BTn3Bp0jrvN2SOuLToac8CpXAHqWLkiJnTTJenDDVF1NA!!/m&ek=1&kp=1&pt=0&bo=4AHxAQAAAAADFyM!&tl=1&vuin=623538278&tm=1592546400&sce=60-4-3&rf=0-0)
![tree2](http://a1.qpic.cn/psc?/V100KQsw1lH6Lb/2u1lLKz1aykDtRBqWOUT3DJkR8F*468cQXIqwmugRwWTPBGMKZLgOpb9jOOWCSLbuuqbsrOyPNs3Y8sUvDECyw!!/m&ek=1&kp=1&pt=0&bo=GAO7AQAAAAADF5M!&tl=1&vuin=623538278&tm=1592546400&sce=60-4-3&rf=0-0)
<br>
從上圖結果可以看出，和分群一樣，有沒有羽毛是超級重要的因素，只要一有羽毛就被歸類成鳥類。其次是哺乳行為，一樣是決定性因素，有哺乳行為就直接是哺乳類。之後再往下看形成較細的枝葉，提供更詳細的判斷方法。
<br>
### 結論
Weka是一個非常方便使用的軟體，因為裏面有許多的常用的演算法，所以它可以處理許多資料探勘的檔，能應對很多種情況，另外其也是open source的軟體，容易使得weka可以更加強大好用，如果能善用此工具，可以事半功倍。<br>
在目前社會上都是資料的環境中，我們要擔心的已經不是手邊沒有資料可以分析，而是煩惱如何有效率地把手邊的資料經過一系列處理後轉化成有用的資訊。
有很多的資訊隱藏在資料的背後，如果能從資料中挖掘出有用的資訊加以運用，可以增加個人或企業的實力。
當資料過於龐大時，如何快速準確的提取出其中有用的資訊對於任何一個資料探勘的工具都是一個挑戰。
<br>
********
參考資料
----
http://weka.sourceforge.net/wekadoc/index.php/en:ARFF_(3.5.6)<br>
http://www.cs.waikato.ac.nz/ml/weka/<br>
http://33tsai.blogspot.com/2008/03/weka.html<br>
http://blog.pulipuli.info/2016/05/weka-weka-j48-decision-tree.html<br>
http://archive.ics.uci.edu/ml/datasets/zoo<br>
