    setwd(“D:/Dropbox/working memory/output/exp2”)
    getwd()

    #讀csv 檔，我把論文資料都放在 dropbox 上，最近他跟我說時間到了空間會消失有點苦惱

    csvpath = “D:/Dropbox/working memory/output/exp2/”
    csvfilesn = list.files( path = csvpath, pattern=”*.csv”)
    tmprt = function(rtcsv){
     read.csv( rtcsv, stringsAsFactors = FALSE, header = TRUE)
    }
    lhudata = lapply(paste(csvpath,csvfilesn, sep = “”), tmprt)
    csvfilesn
    data = lhudata[[1]]

    #這邊會顯示路徑內所有的檔案

    #這是網路上撿別人寫好的 function ，可以把多個 csv 用 bind()合併成新的檔案，本來 csv 沒有給受試者 ID這邊先給受試者ID

    data[‘pID’] = NaN
    for (sz in seq(18)){
     start = (sz-1) * 480 + 1
     end = sz * 480
     for (i in seq(start,end)){
     data$pID[i] = sz
     }
    }

    #因為每個受試者提供 480 筆資料，所以每個數字重複480次之後 +1 帶入

    data[‘ProbeSeq’] = NaN
    data[‘ProbeSeq’] <- c(1, 2)

    #我要比較每個嘗試次裡面第一題表現跟第二題表現有沒有不一樣
    data$Setsize = data$SZ/2

    #初始的 SZ 是紀錄螢幕上出現的色塊有幾個，因為我們只看一組所以要除以二
    data$Feedback <-data$PC

    #紀錄受試者的作答正確還錯誤，因為 PC 之後是拿來算正確率，所以先把他assign 到另外一個變數裡面。

    #接下來處理資料細節，因為只計算正確的，所以 RT 錯誤的先 assign NaN

    data$RT[data$Feedback == 0] = NaN
    #這邊處理 outlier 部份，如果反應時間大於五秒，我們就不採納了
    data$PC[data$RT >= 5] = NaN
    data$RT[data$RT >= 5] = NaN
    summary(data)

    #看一下整體的資料，刪除幾筆資料論文需要回報，接下來產生貝氏統計要用的資料。

    data <- data.frame(aggregate(list(data$Feedback, data$RT), 
     list(data$pID, data$Setsize, data$ProbeType, data$CSI, data$ProbeSeq) ,mean, na.rm = TRUE))
    names(data) <- c(‘pID’, ‘Setsize’, ‘ProbeType’, ‘CSI’, ‘ProbeSeq’,’PC’, ‘RT’) 
    summary(data)

    #把所有要看的變項撈出來算平均，接下來就看計算整體反應時間跟正確率
    tapply(data$PC, data$Setsize, summary)
    tapply(data$PC, data$ProbeType, summary)
    tapply(data$PC, data$CSI, summary)
    tapply(data$PC, data$ProbeSeq, summary)
    tapply(data$RT, data$Setsize, summary)
    tapply(data$RT, data$ProbeType, summary)
    tapply(data$RT, data$CSI, summary)
    tapply(data$RT, data$ProbeSeq, summary)

#接下來就可以處理 BF的部份了

    library(BayesFactor)

#裝好這個套件

#因為我是要跑 ANOVA，所以會需要資料是以 factor 呈現

    data$pID <- factor(data$pID)
    data$Setsize <-factor(data$Setsize)
    data$ProbeType <- factor(data$ProbeType)
    data$CSI <- factor(data$CSI)
    data$ProbeSeq <- factor(data$ProbeSeq)

    #通通變成 factor

    sz.probetype <- anovaBF(PC ~ ProbeType * Setsize + pID, data=data, whichRandom = ‘pID’)

    #正確率（PC）→ IV

    #Setsize &ProbeType→ DV

    #需要一個隨機因子當作 null model 的預測，所以最後加入 pID

    sz.probetype #顯示跑出來的 Bayes Factor

   # =======R 輸出的內容=========
    # [1] Setsize + pID : 8.540596e+70 ±0.84%
    #[2] probetype + pID : 5.644294e+32 ±0.9%
    #[3] Setsize + probetype + pID : 2.152809e+106 ±2.37%
    #[4] Setsize + probetype + Setsize:probetype + pID : 6.090729e+104 ±2.47%

#基本上我的 BF 值都可以是強烈證據支持有效果，尤其是[3]跟[4]的部份，好像交互作用發生機會比較大，但還是想知道說發生機會有多大，所以用下面的指令

    sz.probetype[4]/sz.probetype[3]

    #把 sz.probetype 裡面的[4]跟[3]相除，然後看 Bayes Factor 支持誰發生機率比較大

    # [1] Setsize + probetype + Setsize:probetype + pID :0.02829201 ±3.42%
